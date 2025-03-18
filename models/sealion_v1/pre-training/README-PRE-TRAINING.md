# SEA-LION Pre-Training Setup Guide

## SEA-LION 3B and 7B models are trained on 32 nodes of A100 40GB on AWS EC2

### Software Stack

- AWS Parallel Cluster
- SLURM (Installed with Parallel Cluster)
- Composer and LLM Foundry

### Steps

1. Create key pair
2. VPC creation with web UI (Need NAT gateway)
	1. Use the cluster name as the project name
	2. Check "Enable auto-assign public IPv4 address" in the public subnet

4. Create two S3 buckets
	1. common: for data, checkpoint, and Python source files
	2. mlflow: for MLFlow logging

5. Modify cluster config YAML with:
	1. KeyName
	2. Common S3 bucket name
	3. Public subnet ID for `HeadNode`
	4. Private subnet ID for `SlurmQueues`
	5. Number of p4d.24xlarge instances
	6. Capacity reservation ID

6. Launch with `pcluster` package
	1. Wait for it to finish (around 30+ min)

7. Manually upload a copy of `llm-foundry-<commit hash>.zip` to `s3://<cluster name>-common/source_files`

8. SSH into the head node
   ```
   pcluster ssh -i </path/to/key> -n <cluster name>
   ```

9. Take ownership and change permission of `/fsx/mlflow`
   ```
   sudo chown -R $USER:$USER /fsx/mlflow
   chmod 777 /fsx/mlflow
   ```

10. Clone `nscc_working` to `/fsx` and checkout the `aws-ec2-3b` branch
   ```
   cd /fsx
   git clone https://github.com/aisingapore/nscc_working.git
   cd nscc_working
   git checkout aws-ec2-3b
   ```

11. Start an interactive session to install dependencies
	1. It takes some time to spin up a compute node
	2. It takes some time to build `flash-attn`
    ```
    srun --nodes 1 --ntasks-per-node 1 --cpus-per-task 96 --gres=gpu:8 --time 12:00:00 --pty bash
    sudo apt-get update && sudo apt-get install python3.8-venv
    python3 -m venv /fsx/envs/mosaicml
    source /fsx/envs/mosaicml/bin/activate
    cd </path/to/nscc_working/engr/mosaicml_workspace>
    PYTHONPATH=$(pwd) bash scripts/setup.sh
    ```

12. Launch the training job
    ```
    sbatch launch.slurm
    ```

13. Wait for job to start running and create the MLFlow Server instance (in a separate local terminal)
    ```
    cd </path/to/nscc_working/engr/mosaicml_workspace>
    python scripts/python/create_mlflow_instance.py -n <cluster name> --instance-type <instance type>
    ```
    _Note: Instance type must be available in the cluster's availability zone._

14. Copy content from `fstab_entry`  to `/etc/fstab` and reboot

15. Start the MLFlow server
    ```
    source /fsx/envs/mosaicml/bin/activate
	mlflow server -h 0.0.0.0 --backend-store-uri file:///fsx/mlflow/<model size>-multi-node-sharded/mlruns --no-serve-artifacts
    ```

#### Adding public keys

_Note: this needs to be done on both the head node and the mlflow server instance_

1. Obtain a public key
	1. Either convert the AWS key pair `.pem` file
	   ```
	   ssh-keygen -f </path/to/keypair.pem> -y > </path/to/key.pub>
       ```
       or
	2. Generate a new key pair with a [third party tool](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws)

2. Copy the content of the public key file and append to `$HOME/.ssh/authorized_keys`

#### Launch a new job

1. Modify `launch.slurm`
	1. Change job name to the appropriate model size to log files are name properly

2. Modify `launch.sh`
	1. Change `model_size` to the appropriate model size
	2. Ensure `load_path='null'` and `autoresume='false'`

3. Launch with `sbatch launch.slurm`

#### Resume from latest checkpoint

1. Modify `launch.slurm`
	1. Export `MLFLOW_CONCAT_RUN_ID` with content from `MLFLOW_RUN_ID` found in the base directory. Alternatively, get the "Run ID" from MLFlow web UI.

2. Modify `launch.sh`
	1. Change `autoresume='true'`

#### Resume from previous checkpoint

1. Modify `MLFLOW_CONCAT_RUN_ID` in `launch.slurm` 

2. Modify `launch.sh`
	1. Change `autoresume='false'`
	2. Change `load_path=${S3_BUCKET}/checkpoint/${run_name}/<epoch>-<batch>/<epoch>-<batch>-rank{rank}.pt`

#### Useful commands

- `sinfo`: General queue status
- `squeue`: Running/queued jobs in queue
- `scontrol show nodes`: Display compute node info. `State` is useful for telling why job isn't running yet, e.g., powering up, down, not responding
- `cat /var/log/parallelcluster/clustermgtd`: View cluster management logs

#### Modifications for 3B (32 instances)

#### Create placement group

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html

#### Modify FSx Capacity

1200 -> 7200
Left `PerUnitStorageThroughput` untouched as `7.2*125=900` is more than the throughput spike observed in the 8 instances trial.

Seeing spikes are >900, will increase to 250 throughput

#### Placement group related

#### ParallelCluster creation warning messages

```
{
  "level": "WARNING",
  "type": "PlacementGroupCapacityReservationValidator",
  "message": "When using an open or targeted capacity reservation with an unrelated placement group, insufficient capacity errors may occur due to placement constraints outside of the reservation even if the capacity reservation has remaining capacity. Please consider either not using a placement group for the compute resource or creating a new capacity reservation in a related placement group."
}
```

#### Insufficient capacity

After failing a job due to write permissions (did not `chown` `/fsx/mlfow`), encountered a timeout error message.

```
2023-08-07 05:11:35,692 - [slurm_plugin.clustermgtd:_reset_timeout_expired_compute_resources] - INFO - The following compute resources are in down state due to insufficient capacity: {'queue1': {'p4d24xlarge': ComputeResourceFailureEvent(timestamp=datetime.datetime(2023, 8, 7, 5, 2, 29, 692383, tzinfo=datetime.timezone.utc), error_code='InsufficientInstanceCapacity')}}, compute resources will be reset after insufficient capacity timeout (600.0 seconds) expired
```

Suggested solutions seem to be to just wait it out https://repost.aws/knowledge-center/ec2-insufficient-capacity-errors
