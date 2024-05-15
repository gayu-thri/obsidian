
Hi Malathi,

We have ordered a NFS server machine and our use case is to have an **NFS server-client setup** ready. This is to facilitate ease in accessing data during LLM training as the data size will be huge easily ranging a few TBs and for storage concerns - Thus by, reducing duplicates of data across machines and saving some space.

The scenario in brief, a single machine acts as a NFS server and the rest of the machines exported in server will act as clients. The server will have a shared path configured under which the data stored can be accessed across all the client machines. These clients can then access the data from the shared folder in server directly with/without any credentials. 

Requisitions in server & clients machines are briefed below.
- **Server**: 
	- Setup required in server side
		- Installation of `nfs-kernel-server`
		- Status checks of `nfs-server`
		- Setup of shared directory
		- Export clients
			- Shared path, IP address, Permissions, Sync, etc 
		- Firewall configuration
- **Clients**: 
	- Setup required in client side
		- Installation of `nfs-common`
		- Mount shared directory

If your team has an existing support already to do the above setup, please let us know. If yes, it'd be more helpful if you could provide us the documentation of the APIs.


