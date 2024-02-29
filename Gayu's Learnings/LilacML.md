
#### Installation
- https://docs.lilacml.com/getting_started/installation.html
- From pypi
	- $ *pip install lilac[all]*
- From existing Lilac project
	- $ *docker pull lilacai/lilac*
	```bash
	  docker run -it --gpus all --volume /home/joe/Downloads/lilac-data:/data -p 5432:5432 --platform=linux/amd64 \
	        -e DUCKDB_USE_VIEWS="1" \
	        -e HF_HOME="/data/.huggingface" \
	        -e _SEE_LILAC_DOCS_="https://lilacml.com/huggingface/huggingface_spaces.html" \
	        -e LILAC_PROJECT_DIR="/data" \
	        -e TRANSFORMERS_CACHE="/data/.cache" \
	        -e XDG_CACHE_HOME="/data/.cache" \
	        -e LILAC_AUTH_ENABLED="false" \
	        registry.hf.space/lilacai-lilac:latest
	```
#### References
- https://github.com/lilacai/lilac/issues/737
	- Above docker run command taken from this issue