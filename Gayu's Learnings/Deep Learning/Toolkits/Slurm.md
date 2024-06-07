https://slurm.schedmd.com/sbatch.html
https://medium.com/@laura.hanu10/intro-to-multi-node-machine-learning-2-using-slurm-37acbcebf4f9

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