#### Bookmarks
- [Basic overview by IBM](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)
#### Motivation
- There are two problems in LLMs
	1. No source (Proof for source of response given by the model)
	2. Out of date
- Reduces the need for users to continuously train the model on new data
- RAG helps in solving the above problems
#### Description
- Makes use of additional ___content store___ to give more accurate response
- In brief, the following happens
	- **User Prompt -> LLM**
		- LLM doesn't directly give the response to the user (LLM -> User ❌)
	- **LLM -> Content Store**
		- Retrieves information relevant to user's query
		- Content store can be a list of documents (or) policies (or) any data
	- **{(i) *Instruction to pay attention to content store +* 
	  (ii) *Retrieved relevant info +* 
	  (iii) *User Prompt*} -> LLM**
		- **Three parts** are sent to LLM
#### Results
- Solving "**Out of date**" - The need to adapt the model to a new piece of info
	- No need to fine-tune model on extra data for every new piece of info
	- One could simply add extra documents with relevant data
		- Model can simply refer to this for generating the right & latest response
- Solving "**No source**"
	- It's less likely to do the below, 
		- Rely on data used while training ❌
		- Hallucinate / Leak the data ❌
	- Depends on the primary data source (Evidence)
#### Constraints
- Retriever needs to be trained well for model to give correct response
