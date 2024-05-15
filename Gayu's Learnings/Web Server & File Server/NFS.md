### Network File System (NFS)
- Allows to share files across different machines
- Cross Operating Systems are also supported
	- Ex: Windows (Server) and Linux (Client)
- We need to setup a NFS server and NFS clients for it

---
### Steps to configure NFS Server 

##### (i) Installation & Setup
```bash
apt update 
apt -y install nfs-kernel-server 
systemctl status nfs-server 
mkdir /exports 
mkdir /exports/backups 
```
##### (ii) Export the clients
```bash
vi /etc/exports 
```
> */exports/backups 192.168.0.127(rw,sync,no_subtree_check) *

```bash
exportfs -ar 
exportfs -v 
```
##### (iii) Firewall Configuration
``` bash
ufw allow from 192.168.0.127 to any port nfs 
```

---
### Steps to configure NFS Client 

##### (i) Installation
```bash
apt -y install nfs-common 
```
##### (ii) Mount the shared directory
```bash
mkdir /mnt/backups 
mount 192.168.0.126:/exports/backups /mnt/backups 
vi /etc/fstab 
```

> 192.168.0.126:/exports/backups /mnt/backups nfs auto,nofail,noatime,nolock,tcp,actimeo=1800,_netdev 0 0

---
