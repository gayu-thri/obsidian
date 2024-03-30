Introduction Reference Link
	- [Simple Introduction to Large Language Models (LLMs)](https://www.youtube.com/watch?v=osKyvYJ3PRM)
Two types of Language Models (LMs)
	1. Causal LM
	2. Masked LM
### History
- ![[Pasted image 20240310100332.png]]
### LM Basics
- Data flow
	1. Tokenization
		- Compute embeddings
				- Vectors with ***magnitude*** & ***direction***
				- Captures ***semantic meaning*** & ***relationship*** using similarity
		- Store in vector database
	2. Training
		- Pre-training
			- Foundational diverse model; Slower in training
		- Fine-tuning 
			- Faster in training; Higher accuracy; Specific use-cases
- Metrics used
	- **Perplexity score**
		- Meaningfulness of a sentence
	- **RLHF**
		- Reinforcement Learning Through Human Feedback
		- +ve & -ve scores based on output
- Limitations / Problems
	- **Logical reasoning**
	- **Bias**
		- LLMs don't reflect the real world / history
		- Solution: RAG (Internal search in DB & External search)
	- **Hallucinations**
		- LLMs will be confidently wrong
	- **Cost**
		- Compute power; Resources 
- Use cases
	- Programming Assistants; Summarization; Question Answering; Essay writing; Translation; Image Captioning
- Advancements & Research
	- Knowledge Distillation (Teacher and Student LLM)
	- RAG (Look up information outside training data using DB)
