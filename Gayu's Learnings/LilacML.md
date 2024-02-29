
#### Installation
- **Links**
	- https://docs.lilacml.com/getting_started/installation.html
	- https://docs.lilacml.com/deployment/self_hosted.html
- **From pypi, via command line**
	- $ *pip install lilac[all]*
- **From existing Lilac project, via docker**
	- **ISSUE**: On using the command, opens only a nginx server page
	- $ *docker pull lilacai/lilac*
	- OR
	- $ *git clone https://github.com/lilacai/lilac.git*
	  $ *docker build -t lilac .*
	```bash
	  docker run -it \
  -p 5432:80 \
  --volume /host/path/to/data:/data \
  -e LILAC_PROJECT_DIR="/data" \
  lilac
	```
	- To use all GPUs
		```bash
		 --gpus all 
		```
	- To use a specific GPU
		```bash
		--gpus device=0
		```

- **Command I used and is working** 
	- http://172.21.168.254:5432/
	```bash
	docker run -it --platform=linux/amd64 -p 5432:80 --volume /media/data/gayu/workspace/llm/lilac/:/data -e LILAC_PROJECT_DIR="/data" lilacai/lilac
	```

#### References
- https://github.com/lilacai/lilac/issues/737
	- Above docker run command taken from this issue