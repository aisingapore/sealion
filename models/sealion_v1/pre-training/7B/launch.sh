#!bin/sh

gpus_per_node=${1:-$(nvidia-smi -L | wc -l)}
world_size=${2:-$gpus_per_node}
node_rank=${3:-0}
master_addr=${4:-'127.0.0.1'}
master_port=${5:-$((10000 + $RANDOM % 9000))}
# time-string format:
#     epoch (ep), batch (ba), sample (sp), token (tok), or duration (dur)
# duration is [0.0, 1.0) indicating fraction of training process complete

llmfoundry_dir=$(pip show llm-foundry | grep 'Editable project location')
llmfoundry_dir=${llmfoundry_dir#*: }
script="${llmfoundry_dir}/scripts/train/train.py"

# model_size='mpt-125m'
# model_size='mpt-3b'
# model_size='mpt-13b'
model_size=mpt-7b

experiment_name="${model_size}-multi-node-sharded"
run_number=12
run_name="${experiment_name}-${run_number}"
tracking_uri="${SHARED_FS_DIR}/mlflow/${experiment_name}/mlruns"
# tracking_uri="sqlite:///${SHARED_FS_DIR}/mlflow/${experiment_name}/mlflow.db"

# data_local_path="${SHARED_FS_DIR}/cache/data/my-copy-c4"
# data_remote_path="${S3_BUCKET}/data/my-copy-c4"

data_local_path="${SHARED_FS_DIR}/cache/data/final_for_training"
data_remote_path='null'

# data_local_path="${SHARED_FS_DIR}/cache/data/test_final"
# data_remote_path="${S3_BUCKET}/data/test_final"

tokenizer_name="SEABPETokenizer"
tokenizer_vocab_path="${SHARED_FS_DIR}/tokenizer/256000_wonorm_wdummyprefix.model"
# tokenizer_name=EleutherAI/gpt-neox-20b

config_path="$(pwd)/configs/pretrain/${model_size}.yaml"
# config_path="$(pwd)/configs/pretrain/${model_size}_Ngan.yaml"
# config_path="$(pwd)/configs/pretrain/${model_size}_neox_tokenizer.yaml"

# Path to the checkpoint
# load_path='null'
# load_path="${S3_BUCKET}/checkpoint/${run_name}/ep0-ba88200/ep0-ba88200-rank{rank}.pt"
load_path=/fsx/nscc_working/engr/mosaicml_workspace/checkpoint/${run_name}/ep0-ba222000/ep0-ba222000-rank{rank}.pt
# load_path="${S3_BUCKET}/checkpoint/${run_name}/ep0-ba70500/ep0-ba70500-rank{rank}.pt"
# load_path="${S3_BUCKET}/checkpoint/mpt-13b-multi-node-sharded-5/ep0-ba51900/ep0-ba51900-rank{rank}.pt"
# load_path="${S3_BUCKET}/checkpoint/mpt-13b-multi-node-sharded-8/ep0-ba80100/ep0-ba80100-rank{rank}.pt"
# load_path="/home/ubuntu/checkpoint/${run_name}/ep0-ba46500/ep0-ba46500-rank{rank}.pt"
# load_path="/fsx/nscc_working/engr/mosaicml_workspace/checkpoint/mpt-13b-multi-node-sharded-8/ep0-ba80100/ep0-ba80100-rank{rank}.pt"
save_interval='1000ba' # time-string or integer (in epochs)
# save_interval='500ba' # time-string or integer (in epochs).
# save_interval='10ba' # time-string or integer (in epochs).
save_num_checkpoints_to_keep=1 # Set -1 to keep all checkpoints locally
save_dir="${S3_BUCKET}/checkpoint/${run_name}"
autoresume='false'
# autoresume='true'
# load_ignore_keys="[\"state/optimizers\"]"
# load_ignore_keys="[\"state/optimizers\",\"state/schedulers\"]"
# load_ignore_keys="[\"state/schedulers\",\"state/algorithms\"]"
# load_ignore_keys="[\"state/algorithms\"]"
# load_ignore_keys="[\"state/schedulers\"]"
# load_ignore_keys="[\"state/optimizers\",\"state/schedulers\",\"state/algorithms\"]"
save_overwrite='false'
if [ ! $load_path = 'null' ] && [ $autoresume = 'false' ]; then
    save_overwrite='true'
fi

eval_interval='50000000ba' # time-string or integer (in epochs).
# eval_interval='10ba' # time-string or integer (in epochs).
# Evaluate on this many batches. -1 to iterate over the entire dataloader
# eval_subset_num_batches=-1
eval_subset_num_batches=${world_size}
# eval_first='false' # Evaluate before training begins (maybe for resuming?)
eval_first='false'

# max_duration='267856ba' # time-string or integer (in epochs).
max_duration='1ep'
# === mpt-125m settings ~40GB
# global_train_batch_size=4096 # Has to be divisible by world size
# device_train_microbatch_size=8 # Reduce to global_train_batch_size // world_size if it is smaller
# device_eval_batch_size=8
# === mpt-3b settings ~39GB
# global_train_batch_size=3584 # Has to be divisible by world size
# device_train_microbatch_size=7 # Reduce to global_train_batch_size // world_size if it is smaller
# device_eval_batch_size=7
# global_train_batch_size=3600 # Has to be divisible by world size
# device_train_microbatch_size=5 # Reduce to global_train_batch_size // world_size if it is smaller
# device_eval_batch_size=5
# global_train_batch_size=1200 # Has to be divisible by world size
# device_train_microbatch_size=5 # Reduce to global_train_batch_size // world_size if it is smaller
# device_eval_batch_size=5
# === mpt-13b settings ~38.2GB
# global_train_batch_size=768 # Has to be divisible by world size
# device_train_microbatch_size=3 # Reduce to global_train_batch_size // world_size if it is smaller
# device_eval_batch_size=3
# global_train_batch_size=2048 # Has to be divisible by world size
# device_train_microbatch_size=8 # Reduce to global_train_batch_size // world_size if it is smaller
# device_eval_batch_size=8
global_train_batch_size=2048 # Has to be divisible by world size
device_train_microbatch_size=4 # Reduce to global_train_batch_size // world_size if it is smaller
device_eval_batch_size=4
# global_train_batch_size=256 # Has to be divisible by world size
# device_train_microbatch_size=1 # Reduce to global_train_batch_size // world_size if it is smaller
# device_eval_batch_size=1
precision='amp_bf16'

state_dict_type='sharded'
load_monolith_rank0_only='false'
sync_module_states='false' # Needs to be true for load_monolith_rank0_only=true
use_orig_params='true' # Needs for be false if load_monolith_rank0_only=true
init_device='meta' # Cannot be meta if load_monolith_rank0_only=true

mono_save_interval=999999999
# mono_save_interval=14400
# mono_save_interval=2000
# mono_save_interval=100

loss_monitor_window_size=100
loss_monitor_frequency_threshold=0.6
loss_monitor_magnitude_threshold=0.05
loss_monitor_slope_threshold=0.1
loss_monitor_alert_frequency=1200
loss_monitor_slack_webhook_url=''
loss_monitor_report_ok='true'

throughput_monitor_window_size=100
throughput_monitor_moving_avg_window_size=10
throughput_monitor_split=0.7
throughput_monitor_pvalue_threshold=1e-4
throughput_monitor_drop_threshold=0.975
throughput_monitor_alert_frequency=1200
throughput_monitor_slack_webhook_url=''
throughput_monitor_image_dir="$(pwd)/image"

model_args=" \
    model.init_device=$init_device
    "
data_args=" \
    data_local=$data_local_path \
    data_remote=$data_remote_path \
    train_loader.dataset.split=wo_langid \
    eval_loader.dataset.split=wo_langid_val
    "
tokenizer_args="
    tokenizer_name=$tokenizer_name \
    tokenizer_vocab_file=$tokenizer_vocab_path
    "
checkpoint_args=" \
    run_name=$run_name \
    load_path=$load_path \
    save_interval=$save_interval \
    save_num_checkpoints_to_keep=$save_num_checkpoints_to_keep \
    save_overwrite=$save_overwrite \
    save_folder=$save_dir \
    autoresume=$autoresume
    # load_ignore_keys=$load_ignore_keys
    "
eval_args=" \
    eval_interval=$eval_interval \
    eval_subset_num_batches=$eval_subset_num_batches \
    eval_first=$eval_first
    "
system_and_numeric_args=" \
    max_duration=$max_duration \
    global_train_batch_size=$global_train_batch_size \
    device_train_microbatch_size=$device_train_microbatch_size \
    device_eval_batch_size=$device_eval_batch_size \
    precision=$precision
    "
fsdp_args=" \
    fsdp_config.state_dict_type=$state_dict_type \
    fsdp_config.load_monolith_rank0_only=$load_monolith_rank0_only \
    fsdp_config.sync_module_states=$sync_module_states \
    fsdp_config.use_orig_params=$use_orig_params
    "
callback_args=" \
    callbacks.speed_monitor.window_size=$throughput_monitor_moving_avg_window_size \
    callbacks.mono_ckpt_saver.batch_interval=$mono_save_interval \
    callbacks.loss_monitor.window_size=$loss_monitor_window_size \
    callbacks.loss_monitor.frequency_threshold=$loss_monitor_frequency_threshold \
    callbacks.loss_monitor.magnitude_threshold=$loss_monitor_magnitude_threshold \
    callbacks.loss_monitor.slope_threshold=$loss_monitor_slope_threshold \
    callbacks.loss_monitor.alert_frequency=$loss_monitor_alert_frequency \
    callbacks.loss_monitor.slack_webhook_url=$loss_monitor_slack_webhook_url \
    callbacks.loss_monitor.report_ok=$loss_monitor_report_ok
    callbacks.throughput_monitor.window_size=$throughput_monitor_window_size \
    callbacks.throughput_monitor.moving_avg_window_size=$throughput_monitor_moving_avg_window_size \
    callbacks.throughput_monitor.split=$throughput_monitor_split \
    callbacks.throughput_monitor.pvalue_threshold=$throughput_monitor_pvalue_threshold \
    callbacks.throughput_monitor.drop_threshold=$throughput_monitor_drop_threshold \
    callbacks.throughput_monitor.alert_frequency=$throughput_monitor_alert_frequency \
    callbacks.throughput_monitor.slack_webhook_url=$throughput_monitor_slack_webhook_url \
    callbacks.throughput_monitor.image_dir=$throughput_monitor_image_dir
    "
tracking_args=" \
    loggers.mlflow.experiment_name=$experiment_name \
    loggers.mlflow.tracking_uri=$tracking_uri
    "

if [ ! $load_path = 'null' ] || [ $autoresume = 'true' ]; then
    if [ -z "${MLFLOW_CONCAT_RUN_ID}" ]; then
	echo 'ERROR: Resuming from a previous checkpoint but MLFLOW_CONCAT_RUN_ID environment variable not set.'
	exit 1
    fi
fi

composer \
    --nproc $gpus_per_node \
    --world_size $world_size \
    --node_rank $node_rank \
    --master_addr $master_addr \
    --master_port $master_port \
$script $config_path \
    $model_args \
    $data_args \
    $tokenizer_args \
    $checkpoint_args \
    $eval_args \
    $system_and_numeric_args \
    $fsdp_args \
    $callback_args \
    $tracking_args

