- Input -> Features (Smaller chunks) -> Hashes
- All hashes combined to produce final hash for input

#### Near Duplicate Detection
- Identify & Determine similarity between documents / pieces of text
- Degree of similarity
- Nearly Duplicates -> Rephrased sentences, synonyms, different formatting, etc
- Use cases:
	- Plagiarism, document clustering, information retrieval, content management systems
- Steps
	- Tokenisation
	- Text similarity measures (Cosine / Jaccard Similarity)
	- Hashing methods

#### SimHash
Steps
- Tokenisation
	- Input -> Features
	- Features can be words / n-grams / specific pieces of info like dates, names
- Hashing
	- Hash of each Feature
	- SHA-1 or MD5
- Combining Features Hashes
	- Concatenation / Bit wise operations like XOR

Comparison
- Calculate distance between them
	- Number of different bits in 2 hashes
	- Smaller distance = More similar

#### EXAMPLE

