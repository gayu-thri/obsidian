https://medium.com/@jayantnehra18/effective-data-deduplication-for-training-robust-language-models-44467afac5bb
https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1

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