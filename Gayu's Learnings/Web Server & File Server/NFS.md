### Network File System (NFS)
- Allows to share files across different machines
- Cross Operating Systems are also supported
	- Ex: Windows (Server) and Linux (Client)
- We need to setup a NFS server and NFS clients for it

---
### To verify NFS is running

```bash
showmount -e hostname
```
---
### Steps to configure NFS Server 

##### (o) User account for NFS
```bash
sudo adduser nfsuser
sudo usermod -aG sudo nfsuser
su nfsuser

# Update UID and GID of nfsuser
sudo usermod -u nobody nfsuser
sudo groupmod -g nogroup nfsuser

# Make sure UID & GID are updated
getent passwd nfsuser
```
##### (i) Installation & Setup
```bash
sudo apt update 
sudo apt -y install nfs-kernel-server 
sudo systemctl status nfs-server

# Update permissions
sudo chown nobody:nogroup /home/nfsuser/shared
sudo chmod 777 /home/nfsuser/shared/*
```
##### (ii) Export the clients
```bash
vi /etc/exports 
```
> */exports/backups 192.168.0.127(rw,sync,no_subtree_check,no_root_squash) *
```bash
sudo exportfs -ar 
sudo exportfs -v 
```
- **-ar**: Will show any errors/warnings
- **-v**: To view current active exports
- **-no_subtree_check**
	- System doesn't have to check permissions for every internal folder which will save time
##### (iii) Firewall Configuration
``` bash
ufw allow from 192.168.0.127 to any port nfs 
```

---
### Steps to configure NFS Client 

##### (o) User account for NFS
```bash
sudo adduser nfsuser
sudo usermod -aG sudo nfsuser
su nfsuser

# Update UID and GID of nfsuser
sudo usermod -u nobody nfsuser
sudo groupmod -g nogroup nfsuser

# Make sure UID & GID are updated
getent passwd nfsuser
```
##### (i) Installation
```bash
sudo apt -y install nfs-common 
```
##### (ii) Mount the shared directory
```bash
sudo mkdir -p /home/nfsuser/shared
# Update permissions
sudo chown nobody:nogroup /home/nfsuser/shared
sudo chmod 777 /home/nfsuser/shared/*

sudo mount 192.168.0.126:/home/nfsuser/shared /home/nfsuser/shared

vi /etc/fstab 
```

> 192.168.0.126:/exports/backups /mnt/backups nfs auto,nofail,noatime,nolock,tcp,actimeo=1800,_netdev 0 0

---
NOTE: Make sure to add `/*` when doing `chmod`, to get sub-directory access