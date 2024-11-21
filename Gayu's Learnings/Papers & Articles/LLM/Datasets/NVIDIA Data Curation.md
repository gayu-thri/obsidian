https://arxiv.org/pdf/2407.06380  
NVIDIA Data Curation Paper

Takeaways
- In de-duplication, it is better to prioritise keeping samples from older sources than more recent ones.
- In deduplication, it is better to priortize keeping samples from older sources than more recent ones.
#### 3 Phases of Curation
1. Raw text
2. Post de-duplication
3. Post Quality Filtering

##### De-duplication
- Both exact and fuzzy 
- Exact
	- 128-bit hash for each document
	- Group docs by hashes
	- Select one doc per group (In addtn. to fuzzy)

##### Quality Filtering
- De-duplicated docs - filtered based on perplexity of KenLM model
