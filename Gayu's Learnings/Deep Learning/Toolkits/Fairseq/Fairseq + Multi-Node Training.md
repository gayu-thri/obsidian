
- https://github.com/facebookresearch/fairseq/issues/1855
- Generally you just need to set `--distributed-port` and `--ntasks-per-node 1`. Something like this should work: 
```bash
srun --nodes 2 --gres=gpu:8 --ntasks-per-node 1 fairseq-train --distributed-port 12345 --no-save --disable-validation --task dummy_masked_lm --arch dummy_model --optimizer sgd --lr 1e-4 --max-sentences 8 --tokens-per-sample 512 --dataset-size 10000 --max-epoch 1 --dict-size 49995 --log-interval 10
```

fairseq_slurm.sh
```bash
#!/bin/bash

# =================================================================

# Resource requirements

# =================================================================

#SBATCH --nodes=2

#SBATCH --wait-all-nodes=1

#SBATCH --nodelist=X,Y

#SBATCH --ntasks-per-node=1

#SBATCH --cpus-per-task=10

#SBATCH --gres=gpu:1

#SBATCH --exclusive

#SBATCH --time=24:00:00

#SBATCH --partition=LocalQ

#SBATCH --output=dialogsum_fairseq_training_%j.out

#SBATCH --error=dialogsum_fairseq_training_%j.err

#SBATCH --job-name=dialogsum_fairseq_training

  

# =================================================================

# Activate the conda environment

# =================================================================

source /home/gayu/miniconda3/bin/activate fairseq

  

# =================================================================

# Load the necessary modules

# =================================================================

# NOTE: Environment variables need to be exported from within slurm

  

# socket interface name from ifconfig

export NCCL_SOCKET_IFNAME=bond0

export NCCL_DEBUG=INFO

export TORCH_DISTRIBUTED_DEBUG=INFO

export LOGLEVEL=INFO

export PATH=/home/gayu/.local/bin:$PATH

export PYTHONPATH=/home/gayu/miniconda3/envs/fairseq/bin/python

echo "NODELIST="${SLURM_NODELIST}

  

nodes=( $( scontrol show hostnames $SLURM_JOB_NODELIST ) )

echo Node : $nodes

echo $nodes_array

echo The value of NCCL SOCKET IFNAME is: $NCCL_SOCKET_IFNAME

echo The value of NCCL DEBUG is: $NCCL_DEBUG

echo path : $PATH

echo python_path : $PYTHONPATH

  

echo Slurm job num nods : $SLURM_JOB_NUM_NODES

  

# =================================================================

# Run the distributed training

# =================================================================

export CUDA_VISIBLE_DEVICES=4

srun --label \

fairseq-train \

data-bin/dialogsum \

--task language_modeling \

--save-dir checkpoints/dialogsum \

--arch transformer_lm \

--share-decoder-input-output-embed \

--dropout 0.1 \

--optimizer adam \

--adam-betas '(0.9, 0.98)' \

--weight-decay 0.01 \

--clip-norm 0.0 \

--lr 0.0005 \

--lr-scheduler inverse_sqrt \

--warmup-updates 4000 \

--warmup-init-lr 1e-07 \

--tokens-per-sample 512 \

--sample-break-mode none \

--max-tokens 2048 \

--update-freq 16 \

--fp16 \

--max-update 50000 \

--distributed-port=12345 \

# --distributed-world-size=2 \

# --distributed-init-method "tcp://$(hostname -i):12345" \
```