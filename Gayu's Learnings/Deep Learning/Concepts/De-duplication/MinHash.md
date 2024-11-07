Source: https://huggingface.co/blog/dedup

---
#### General Workflow
- Shingling (Tokenization)
- Fingerprinting (MinHash)
	- Each doc -> Set of hashes
- Locality-sensitive hashing (LSH)
	- Groups docs with similar bands together
	- To reduce no. of comparisons
	- Duplicate removal
---
#### Shingles
- Tokenization of document
- N-grams a.k.a shingles
- Example of world-level tri-grams

| doc_id | shingles                                                                        |
| ------ | ------------------------------------------------------------------------------- |
| 0      | {"Deduplication is so", "is so much", "so much fun"}                            |
| 1      | {'so much fun', 'fun and easy', 'Deduplication is so', 'is so much'}            |
| 2      | {'dog is a', 'is a thing', 'wish spider dog', 'spider dog is', 'I wish spider'} |
- Time complexity = O(NM)
	- N - documents; M - length of documents
- Scale-able with parallelisation

----
#### Fingerprint Computation
- Each shingle either be
	- 1) hashed multiple times with different hash functions
	- 2) permuted multiple times using one hash function
- Examples
	- Permute each hash 5 times
	- ![[Pasted image 20241101073030.png]]
	- Take minimum value of each column within each document (<**MIN**> part of MinHash)
		- ==***DOUBTFUL***==
	- Minimum (Most common choice)
	- Other order statistics: Maximum, kth smallest or kth largest can be used as well
--- 
#### LSH
- Fingerprint Array -> Bands
- Each band - same number of rows
	- Any hash values left are ignored
- Example
	- b=2 bands and r=2 rows to group those documents
	- ![[Pasted image 20241101075020.png]]
	- two documents have same hash at band index -> clustered into same bucket
		- ![[Pasted image 20241101075245.png]]

---
### Beyond Duplicate Pairs

Two options
- (i) Double-check Jaccard similarities - by calculating shingle overlap
	- Jaccard similarity = (A intersection B) / (A U B) 
	- BigCode followed this; Worked reasonably well
- (ii) Treat as True Positives
	- A similar to B; B similar to C
	- A and C MAY NOT BE similar
		- Considering like this, will save time
	- RECOMMENDED:
		- Going over dataset, make a decision looking at duplicates.

#### Construction of Graph
- Pairs as edges
- Duplicates clustered into connected components
	- No support for `groupby` in `datasets`
- Other options for grouping
	- 