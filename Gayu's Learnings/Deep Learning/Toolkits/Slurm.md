https://slurm.schedmd.com/sbatch.html
https://medium.com/@laura.hanu10/intro-to-multi-node-machine-learning-2-using-slurm-37acbcebf4f9

## Issues in Slurm Setup

- Job credential expired
	- Solution 1:
		- Update the **UID and GID to be the same across all the nodes** participating in slurm setup
	- Solution 2: 
		- Took reference from slurm's FAQ document  
		  
		  >Why are jobs allocated nodes and then unable to initiate programs on some nodes?  [https://slurm.schedmd.com/faq.html](https://slurm.schedmd.com/faq.html)  
	        Suspected reason: Timestamp being inconsistent across nodes
	      
		- **Timestamp should be consistent across all the nodes** participating in slurm setup  
		  
		  Solved it with the below commands on both the machines that I was testing  
		    ```  
		    $ timedatectl set-ntp false  
		    # Manualy set according to local time  
		    $ sudo timedatectl set-time "2024-06-10 16:12:00"  
		    $ sudo timedatectl set-ntp true  
		    ```
		- Note: Do not use NTP for now (Santha suggested) as we need to ask sysadmin

## Quick commands

- To check slurm version
```bash
$ slurmd --version
```
- To check nodes configured
```bash
$ sinfo
```
- To submit a job
```bash
$ sbatch --begin now slurm.sh
```
- To cancel a job
```bash
$ scancel <job_id>
```
- To inspect job details
```bash
$ scontrol show job <job_id>
```
- To check jobs on queue
```bash
$ squeue
```
- To authenticate master node
```bash
$ munge -n | ssh zlabs-gamd13 unmunge
```

## Script to execute

#!/bin/bash

# =================================================================

# Resource requirements

# =================================================================

#SBATCH --nodes=2

#SBATCH --wait-all-nodes=1

#SBATCH --nodelist=zlabs-gamd11,zlabs-gamd2

#SBATCH --ntasks-per-node=1

#SBATCH --gres=gpu:1

#SBATCH --exclusive

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

export CUDA_VISIBLE_DEVICES=4,5

srun --label fairseq-train \

/home/gayu-nfs/shared/data-bin/dialogsum \

--task language_modeling \

--save-dir checkpoints/dialogsum \

--keep-best-checkpoints 3 \

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

--max-update 100000 \

--distributed-port=29403 \

--log-interval 2 \

--log-format tqdm

# --distributed-world-size=2 \

# --distributed-init-method "tcp://$(hostname -i):12345" \