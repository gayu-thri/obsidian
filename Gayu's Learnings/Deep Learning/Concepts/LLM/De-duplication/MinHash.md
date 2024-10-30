Source: https://huggingface.co/blog/dedup

---
**General Workflow**
- Shingling (Tokenization)
- Fingerprinting (MinHash)
	- Each doc -> Set of hashes
- Locality-sensitive hashing (LSH)
	- Groups docs with similar bands together
	- To reduce no. of comparisons
	- Duplicate removal
---
**Shingles**
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