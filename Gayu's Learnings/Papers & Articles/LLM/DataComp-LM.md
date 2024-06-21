https://arxiv.org/pdf/2406.11794

#### De-duplication

- Strategy used in pipeline: 
	- ==Near-duplicate Bloom filtering==
		- Modified version for improving scaling
- Commonly used methods
	- Hash-based:
		- Bloom filters
		- Suffix array-based
		- MinHash-based - MinHashLSH
	- Model-based:
		- [SemDeDup](https://arxiv.org/abs/2303.09540) & D4
- Other considerations:
	- 2 stage de-duplication pipeline
		- Steps
			- 1) Near duplicates removed - **Inter-document** (MinHash)
			- 2) Remove any substring of predetermined length occurs >1 - **Intra-document**
		- Cons
			- Can include docs such as 
				- (a) exact copies of entire doc
				- (b) docs where majority text is duplicate; But unique diff in just header/footer
				- (c) docs significant unique text; Massively repeated boilerplate
	- **MinHash**
		- Locality-sensitive hashing technique (LSH) - Group sets based on Jaccard similarity
		- Hyperparameters: 
			- ngram-size, permutations
			- Following Lee et al., Penedo et al.
			- Prior work:: ngrams=5; jaccard_similarity=0.8, permutations=9000 (Overly expensive)
				- split -> 450 buckets of 20 hashes each 
			- For DCLM ablations, permutations=1,395 (split -> 93 buckets of size 15)
		- ==Doc-level de-duplication -> Doc vs Doc level==
		
	- **Suffix arrays**
		- Introduced in Manber & Myers
		- Use case: Efficient identification & removal of sub-strings of large text corpus 
		- Steps
			- (i) Concatenate all text in corpus together
			- (ii) Sort each suffix
		- Scan this sorted list,
			- Substrings of common prefix easily found - using prefices of neighbours (can be done in parallel fashion)
			- Codebase provided in Lee et al. [88] is not done in a multi-node fashion and requires loading the entire corpus into RAM.

	- **Bloom filters**
		- Bloom filter = Data structure 
			- Enables space-efficient set membership queries
			- Maintains sketch of a set
				- ***Insert*** operation
				- Probabilistic ***membership_query*** operation
					- True/False (For an element in the set)
		- First used for exact-duplicate removal
			- Now extended to perform near-duplicate document and paragraph removal in a tool known as **BFF (Big Friendly Filter)**
		- Vastly >efficient than a MinhHash and SuffixArray pipeline
		- ==Doc-level de-duplication -> Doc vs Corpus level== (in BFF)
		
	- **Paragraph + document BFF**
		- Modified Bloom filter based de-duplication algorithm
		- Initialisation (Bloom filter with fixed size & num_hashers)
			- Estimate of num_tokens
			- Desired false-positive rate (ϵ)
		- Optimal num_hashers (k) = - (ln ϵ) / (ln 2)
		- Find optimal value for **m**
			- ![[Pasted image 20240621143449.png]]
			- Trivial to use binary search algorithm
		- Once bloom filter is established, steps below followed
		- Each doc in corpus,
			- Tokenize doc - UniSeg tokenizer
			- Break doc -> paragraphs (Split using \n)
			- Maintain total_ngrams, contained_ngrams
			- Each paragraph in doc,
				- If ***paragraph < min_ngram_size***, remains
				- If ***min_ngram_size < paragraph < max_ngram_size*** (inclusive), total_ngrams incremented
					- Check this ngram's membership in Bloom filter
						- If present, 
							- it is removed from paragraph
							- Increment contained_ngrams
						- Otherwise, add to bloom filter
				- If ***paragraph > max_ngram_size***
					- Each ngram with size = max_ngram_size increments total counter
						- Check this ngram's membership in Bloom filter
						- If present, 
							- it is removed from paragraph
							- Increment contained_ngrams
							- If >threshold ngrams in para contained in Bloom filter,
								- Entire paragraph is removed from doc
						- Otherwise, add to bloom filter
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