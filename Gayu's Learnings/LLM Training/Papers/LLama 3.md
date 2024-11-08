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
	- Ex: ==Standard dense transformer model architecture with minor adaptions **RATHER THAN MoE model**== - *To maximise training stability*
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
		- Align model with ==HUMAN FEEDBACK==
		- SFT on instruction tuning data
		- Direct Preference Optimisation
		- ==TOOL-USE== - improves coding & reasoning

##### PRE-TRAINING
- Curation & Filtering of dataset
	- De-duplication (URL-level, document-level, line-level)
- Model architecture & scaling laws
- Efficient pre-training techniques at large scale
- Development of recipe

- Annealing data training
	- LR of 50% trained Llama 3 8B model -> 0 (on 4B tokens)
	- New data: 30% weight
	- Default data mix: 70% weight
	- NOTE: Evaluate new data source >>> efficient than performing scaling law experiments for every small dataset.

> During pre-training on the final 40M tokens, we linearly annealed the learning rate to 0, maintaining a context length of 128K tokens. During this annealing phase, we also adjusted the data mix to upsample data sources of very high quality

>In the final stages of pre-training, we train on long sequences to support context windows of up to 128K tokens. We do not train on long sequences earlier because the compute in self-attention layers grows quadratically in the sequence length.

>We increase the supported context length in increments, pre-training until the model has
successfully adapted to the increased context length. We assess successful adaptation by measuring whether (1)model performance on short-context evaluations has recovered completely and (2) the model perfectly solves “needle in a haystack” tasks up to that length.


---
#### MODEL ARCHITECTURE
- Dense ==Transformer== architecture
- Performance gains <- Primarily driven by improvements in **data quality & diversity**
- Modifications compared to Llama 2:
	- ==**Grouped Query Attention (GQA)**== 
		- 8 key-value heads
		- Inference speed up
		- Reduce key-value cache size during decoding
	- Attention mask - prevent self-attention between different documents within the same sequence
		- Important in continued pre-training on very long sequences
	- ==**Vocabulary = 128k tokens**==
		- 100k from tiktoken tokenizer
		- 28k extra to better support non-English
	- **==Activation function = SwiGLU==**
	- **==Positional Embeddings = RoPE==**
		- Base frequency = 5,00,000
		- *To support longer contexts* (up to 32k)
	- 8B model
		- Layers = 32
		- Model dimension = 4,096
		- FFN dimension = 14,336
		- Attention heads = 32
		- Key/Value heads = 8
		- Peak Learning rate = 3 x 10^-4

---

##### POST-TRAINING
- SFT -> DPO
- Reward model and an LM
- Reward model
	- On top of pre-trained checkpoint 
	- Human-annotated preference data
- 
