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