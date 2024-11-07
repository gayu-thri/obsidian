
1. to_hash.py
	- **get_document()**
		- returns doc, file_path, doc_id
		- doc = content read from the file (Ex: json.load())
	- **to_minhash()**
		- input = chunks of docs
		- Note: Uses MinHash from datasketch
		- Steps
			- (i) Normalization using NFC
			- (ii) MinHash
			- (iii) Add to bucket (file_name, doc_id, hash)
	- 