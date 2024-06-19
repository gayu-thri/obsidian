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
- **a) setup_listening_socket()**
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

- **(b) enter_server_loop()**
	- while(1)
		- **accept()**:
			- When accept() is called on listening socket, it blocks until client connects to it
			- When client connects to server,
				- accept() returns client socket - use with read() & write() system calls

To understand how HTTP works...
- Start a python server on a port in local machine (`sudo python3 -m http.server 8000`)
- Curl command on the same (`curl -v http://127.0.0.1:8000`)
	- Output of curl is as below
	- * - comments
	- > - part of request curl sent to our server (**> GET / HTTP/1.1**)
	- < - part of response it gets back from our server - Python server
	- content sent back - index.html
- HTTP request
	- Headers (HTTP method, name of resource client wants (static/dynamic content, etc)
		- Each header ends with a \r\n 
		- Server knows client is done sending headers when there is a empty line with just \r\n
	- Content in body

- **(c) handle_client()**
	- while(1)
		- get_line() function is called - Reads client socket character-by-character - Until it sees \r\n sequence
		- **handle_http_method()**
			- Pass type of HTTP method,resource path
			- call respective handle methods like handle_get_method(), etc
				- _app_get_routes() for _handle_get_method()
	- ZeroHTTPd
		- ZeroHTTPd handles only GET/POST
		- All files it servers - under `public/`
		- request path ends in a `/`, it looks for `index.html`
	- When resource is found,
			- `send_headers()` and `transfer_file_contents()`
	- **sendfile()** for Reading and writing a file
		- Mostly read chunks of source into a buffer. 
			- Reading a file -> transferring data to user space
			- Writing a file -> copying data from user space back to kernel space. 
		- Expensive operations and involve multiple context switches - `read()` and `write()`system calls. 
		- Kernel guys came up with the `[sendfile()](http://man7.org/linux/man-pages/man2/sendfile.2.html)` system call 
			- Takes 2 file descriptors, an offset and length to copy and does the whole copy operation right in the kernel without the buffer copy operations 
			- Avoids multiple context switches caused due to making system calls. 
		- We use `sendfile()` to immensely simplify the data transfer operation to the client socket

- Any new client connections - queued for accept() to retrieve them (Iterative server)
- If the server is not designed to somehow call `accept()` and remain blocked on it while it is serving requests from other clients, ***client requests will queue up. This is the main problem with this iterative server.***