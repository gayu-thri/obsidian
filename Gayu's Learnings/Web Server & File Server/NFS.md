### Network File System (NFS)
- Allows to share files across different machines
- Cross Operating Systems are also supported
	- Ex: Windows (Server) and Linux (Client)
- We need to setup a NFS server and NFS clients for it

---
### To verify NFS is running

```bash
plaintext-ibm
showmount -e hostname
```
---
### Steps to configure NFS Server 

##### (i) Installation & Setup
```bash
sudo apt update 
sudo apt -y install nfs-kernel-server 
sudo systemctl status nfs-server 
mkdir /exports 
mkdir /exports/backups 
```
##### (ii) Export the clients
```bash
vi /etc/exports 
```
> */exports/backups 192.168.0.127(rw,sync,no_subtree_check) *

- *no_subtree_check*
	- System doesn't have to check permissions for every internal folder which will save time
```bash
sudo exportfs -ar 
sudo exportfs -v 
```
- **-ar**: Will show any errors/warnings
- **-v**: To view current active exports
##### (iii) Firewall Configuration
``` bash
ufw allow from 192.168.0.127 to any port nfs 
```

---
### Steps to configure NFS Client 

##### (i) Installation
```bash
sudo apt -y install nfs-common 
```
##### (ii) Mount the shared directory
```bash
mkdir /mnt/backups 
mount 192.168.0.126:/exports/backups /mnt/backups 
vi /etc/fstab 
```

> 192.168.0.126:/exports/backups /mnt/backups nfs auto,nofail,noatime,nolock,tcp,actimeo=1800,_netdev 0 0

---
