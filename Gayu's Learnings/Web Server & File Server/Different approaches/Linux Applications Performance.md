https://unixism.net/2019/04/linux-applications-performance-introduction/

1. [Part I. Iterative Servers](https://unixism.net/2019/04/28/linux-applications-performance-part-i-iterative-servers/)
2. [Part II. Forking Servers](https://unixism.net/2019/04/28/linux-applications-performance-part-ii-forking-servers/)
3. [Part III. Pre-forking Servers](https://unixism.net/2019/04/28/linux-applications-performance-part-iii-preforked-servers/)
4. [Part IV. Threaded Servers](https://unixism.net/2019/04/28/linux-applications-performance-part-iv-threaded-servers/)
5. [Part V. Pre-threaded Servers](https://unixism.net/2019/04/28/linux-applications-performance-part-v-pre-threaded-servers/)
6. [Part VI: poll-based server](https://unixism.net/2019/04/28/linux-applications-performance-part-vi-polling-servers/)
7. [Part VII: epoll-based server](https://unixism.net/2019/04/28/linux-applications-performance-part-vii-epoll-servers/)

---


### Iterative servers
 - Serves **one client after the other** in a single process
 - While client is being served, **other requests are queued by OS**
 - **No concurrency**
	 - Serves exactly one client at a time

### ZeroHTTPd

#### (i) Server socket setup
- 2 CLI arguments
	1. Server port (Default: 8000)
	2. Redis server IP address (Default: 127.0.0.1 - local machine)
- **setup_listening_socket()**
	- Creates a pipe for server to read & write
		- **`s` `=` `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`**
		- socket.AF_INET: Address-family ipv4
		- socket.SOCK_STREAM: connection-oriented TCP protocol
	- Tell OS, it's ok to reuse this socket's address
- **TIME_WAIT state**
	- Ran server, stopped & restarted it immediately after serving at least 1 client
		- Won't bind on port 8000 - client connections go into TIME_WAIT state - OS waits for leftover data to be transferred 
		- Prevents quick restarts
- **SO_REUSEADDR**
	- Lets OS reuse address & bind()
- Describe socket's address
```
	bzero(&srv_addr, sizeof(srv_addr));
	srv_addr.sin_family = AF_INET;
	srv_addr.sin_port = htons(port);
	srv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
```
- Socket address
	- Address & port
	- If server has >1 N/W interface with its own unique address 
	- `INADDR_ANY`, we bind to all available interfaces. `localhost` or `127.0.0.1`
	
- **bind() & listen() system calls turn a program into a N/w server**
	- bind() system call
		- Binds address & port to a socket
		- Allowing clients to reach it
	- listen() system call
		- Converts a socket into listening socket

- Queue length - Determines no. of waiting clients (Until request is accepted as parameter of listen())

- enter_server_loop()
	- while(1)
		- **accept()**:
			- When accept() is called on listening socket, it blocks until client connects to it
			- When client connects to server,
				- accept() returns client socket - use with read() & write() system calls

Current reading pointer: To understand how HTTP works...
#### (ii) Client socket setup
