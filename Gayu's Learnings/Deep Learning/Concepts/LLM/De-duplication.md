https://medium.com/@jayantnehra18/effective-data-deduplication-for-training-robust-language-models-44467afac5bb
https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1
Conceptual references
- https://mattilyra.github.io/2017/05/23/document-deduplication-with-lsh.html
- http://infolab.stanford.edu/~ullman/mmds/ch3.pdf
- https://github.com/Cerebras/modelzoo/tree/main/src/cerebras/modelzoo/data_preparation/nlp/slimpajama (Refer to its readme for understanding about their pipeline)
---
## My notes

#### Existing Strategies
- MinHash, LSH
	- Modified version in SlimPajama scales more easily
- Near-Duplicate Bloom Filtering 
	- Modified version in DataComp-lm scales more easily
#### Abouts
Two types
1. Lexical
2. Semantic

With de-duplicated data,
- Unbiased model training
- Only unique computations; Faster training
- Model generalises well

##### Lexical de-duplication
- Targets ==exact or near-exact matches== in the text
- Steps
	1. Normalise text
	2. Tokenisation
	3. MinHash and LSH

##### Semantic de-duplication
- Targets ==similar in meaning but necessarily in wording== in the text
- Steps
	1. Sentence Embeddings
	2. FAISS (Facebook's) for Efficient Similarity Search
		1. Select the most representative text from the cluster with duplicates

