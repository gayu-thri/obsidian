- Llama 3 - Herd of models
- Multilingual, coding, reasoning & tool usage
- Largest: 405B parameters & context window 128k tokens
- 8B, 70B and 405B parameters
- On par with leading language models such as GPT-4
  
##### GENERIC INFO
- 2 main stages of models:
	- (1) Pre-training - Massive scale using straightforward tasks like **next-word prediction or captioning**
	- (2) Post-training - Tuned to follow instructions & improve specific capabilities (coding, reasoning, etc) 

- 3 key levers for high-quality foundation models
	- (1) Data
	- (2) Scale
	- (3) Managing Complexity

- Pre-training data: Careful pre-processing & curation pipelines
- Post-training data: Filtering approaches & quality assurance

- Architecture
	- Maximise ability to SCALE MODEL DEV PROCESS
	- Ex: Standard dense transformer model architecture with minor adaptions **RATHER THAN MoE model** - *To maximise training stability*
- Training
	- Relatively simple post-training procedure
		- SFT, Rejection sampling, Direct preference optimisation (DPO) RATHER THAN complex reinforcement learning algorithms (*less stable; hard to scale*)

##### LLAMA OVERVIEW
- 2 main stages of model:
	- (1) Pre-training
		- Next-token prediction
		- Model learns STRUCTURE OF LANGUAGE, WIDE KNOWLEDGE ABOUT WORLD
		- 405B parameters - 15.6T tokens - Context window: 8k tokens
	- (2) Continued pre-training
		- Increase context window to 128k tokens
	- (3) Post training
		- 