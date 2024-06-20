https://arxiv.org/pdf/2406.11794

#### De-duplication

- Strategy used: 
	- ==Near-duplicate Bloom filtering==
		- Modified version for improving scaling
- Commonly used methods
	- Hash-based:
		- Bloom filters
		- Suffix array-based
		- MinHash-based - MinHashLSH
	- Model-based:
		- [SemDeDup](https://arxiv.org/abs/2303.09540) & D4
- 
#### Model based filtering approaches
1. **PageRank** score filtering
2. **Semantic deduplication** - similar info
3. **Linear classifiers** fit on pre-trained BGE text embeddings
4. **AskLLM** - prompts LM to see if a doc is helpful
5. **Perplexity filtering** - Retain low perplexity sequences - Following CCNet
6. **Top-k average logits** - Avg top-k model logits over all words in doc (confidence score)
	- Correct words are within k reasonable choices
7. **fastText** - Binary classifiers - data quality

#### Text Classifiers
- For training classifiers,
	- ~400k documents split equally between +ve & -ve classes
		- Different options for +ve data
		- Fix -ve data from RefinedWeb
	- **Perplexity filtering** and **Top-k average logits**:
		- 154M Causal Transformer (Mix of en wiki, subset of books RedPajama v1, pes2o)
		- ==fastText-based filtering outperforms all approaches==

- Text classifier ablations:
	- +ve data -> Wiki, OpenWebText2, RedPajama-books (GPT-3 reference data), OpenHermes 2.5, high-scoring posts from ELI5 subreddit
	- ==fastText OH-2.5 + ELI5 approach -> +3.5% better CORE score than above choices==
	- ==Top-10% examples fairly strict threshold helps==
	- ![[Pasted image 20240620125056.png]]