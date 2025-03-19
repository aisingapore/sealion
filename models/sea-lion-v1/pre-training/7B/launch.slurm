#!/bin/bash

#SBATCH --job-name=mpt-7b-32nodes-final
#SBATCH --nodes=32
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=96
#SBATCH --gres=gpu:a100:8
#SBATCH --time=2440:00:00
#SBATCH --output=log/%x-%j.log

set -e

[ -d log ] || mkdir log

# AWS config
export TZ='Asia/Singapore'
export TMPDIR=/fsx/tmp
export SHARED_FS_DIR=/fsx
export SHARED_OPT_DIR=${SHARED_FS_DIR}/opt
export AWS_OFI_DIR=${SHARED_OPT_DIR}/aws-ofi-nccl
export CUDA_DIR=/usr/local/cuda-11.8
export EFA_DIR=/opt/amazon/efa
export NCCL_DIR=${SHARED_OPT_DIR}/nccl
export OPENMPI_DIR=/opt/amazon/openmpi

export PATH=${CUDA_DIR}/bin:${OPENMPI_DIR}/bin:${PATH:+:${PATH}}

[ ! -d $SHARED_OPT_DIR ] && mkdir $SHARED_OPT_DIR
[ -d $TMPDIR ] || mkdir -p $TMPDIR
rm -rf ${TMPDIR}/*

# Install NCCL and EFA iff CUDA and EFA are present
if [ -d $CUDA_DIR ] && [ -d $EFA_DIR ]; then
    if [ ! -d $NCCL_DIR ]; then
        echo 'Installing NCCL ...'
        cd $SHARED_OPT_DIR
        git clone https://github.com/NVIDIA/nccl.git
        cd $NCCL_DIR
        make -j src.build
    fi
    if [ ! -d $AWS_OFI_DIR ]; then
        echo 'Installing aws-ofi-nccl'
        cd $SHARED_OPT_DIR
        AWS_OFI_VER=1.7.1
        wget https://github.com/aws/aws-ofi-nccl/releases/download/v${AWS_OFI_VER}-aws/aws-ofi-nccl-${AWS_OFI_VER}-aws.tar.gz
        tar -xf aws-ofi-nccl-${AWS_OFI_VER}-aws.tar.gz
        cd aws-ofi-nccl-${AWS_OFI_VER}-aws
        ./configure --prefix=${AWS_OFI_DIR} --with-mpi=${OPENMPI_DIR} --with-libfabric=${EFA_DIR} --with-cuda=${CUDA_DIR} --enable-platform-aws
        make
        make install
    fi
fi

cd $SLURM_SUBMIT_DIR
export PYTORCH_CUDA_ALLOC_CONF="max_split_size_mb:128"
export LD_LIBRARY_PATH=${NCCL_DIR}/build/lib:${CUDA_DIR}/lib64:${CUDA_DIR}:${EFA_DIR}/lib:${OPENMPI_DIR}/lib:${AWS_OFI_DIR}/lib${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export FI_PROVIDER='efa'
export FI_EFA_USE_DEVICE_RDMA=1
export NCCL_DEBUG=INFO
export SLURM_CLUSTER_NAME='seafm-cluster-2'
# Composer/LLM Foundry env vars
export S3_BUCKET="s3://${SLURM_CLUSTER_NAME}-common"
export MLFLOW_CONCAT_RUN_ID=fc6e42f2d1d84530ad9d93f3a9a62ed1
export COMPOSER_UPLOAD_STAGING_FOLDER="${SHARED_FS_DIR}/staging"
export TRITON_CACHE_DIR="${SHARED_FS_DIR}/cache/triton"

[ -d $COMPOSER_UPLOAD_STAGING_FOLDER ] || mkdir -p $COMPOSER_UPLOAD_STAGING_FOLDER
rm -rf "${COMPOSER_UPLOAD_STAGING_FOLDER}/*"

source "${SHARED_FS_DIR}/envs/mosaicml/bin/activate"

gpus_per_node=$SLURM_GPUS_ON_NODE
world_size=$(($gpus_per_node * $SLURM_JOB_NUM_NODES))
master_addr=$(scontrol show hostnames $SLURM_JOB_NODELIST | head -n 1)
master_port=$((10000 + $RANDOM % 9000))

log_dir="$(pwd)/log/${SLURM_JOB_NAME}"
mkdir -p $log_dir

srun_args=" \
    --wait=60 \
    --kill-on-bad-exit=1 \
    "
cleanup_cmd=" \
    python -c 'import streaming; streaming.base.util.clean_stale_shared_memory()' \
    "
launch_cmd=" \
    PYTHONPATH=$(pwd) \
    bash launch.sh \
    $gpus_per_node \
    $world_size \
    \$SLURM_PROCID \
    $master_addr \
    $master_port \
    "
echo $launch_cmd

srun $srun_args --jobid $SLURM_JOBID bash -c "${cleanup_cmd}; ${launch_cmd}" 2>&1 | tee -a "${log_dir}/main.log"
