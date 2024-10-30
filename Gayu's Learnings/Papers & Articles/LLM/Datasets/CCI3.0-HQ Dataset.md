- Large scale Chinese dataset
- High quality; Pre-training dataset
- 500 GB subset of Chinese Corpora Internet (CCI3.0)
- 2-stage hybrid filtering pipeline

Proposed in paper:
- **CCI3-HQ classifier,** an advanced quality classification tool that significantly
improves data selection processes in LLM training.

---
**Generic**
- Demand for pre-training data exceeded 10T tokens
- Key trajectories in English pre-training: 
	- Scaling & Quality
- Focus shifted from rule-based filtering -> model-driven approaches
	- (redpajama -> fineweb-edu)
---

**Data Curation Pipeline**
- Raw data -> ==Fundamental processing== -> CCI 3.0 Dataset 
- CCI 3.0 Dataset -> ==High Quality processing== -> CCI 3.0 - HQ Dataset

- Fundamental stage
	- Safety filtering
	- Text extraction and cleaning       (*Special parsers*)
	- De-duplication        (*Global MinHash*; *Removes near-duplicate docs*)
	- Initial Quality Assessment         (*Using basic model score*) 
		- Filter low-quality docs
		- Eliminate outliers
		- Reduce repetition
		- Basic quality classifier -> Predicts likelihood of text being referenced in reliable sources
- HQ stage
	- Employs ==Qwen2-72B-Instruct to identify high-quality samples==
	- Train a 0.5B **==quality classifier==** on 140k training samples
	
**NOTE**: Our proposed quality classifier classifier(CCI3.0-HQ 5) achieved
superior performance, surpassing the classifier(FineWeb-edu 6), classifier(IndustryCorpus2 7) , and classifier(ChineseWebText 8) in terms of
F1 score.

**HQ Stage In Detail**
- Qwen2-72B-Instruct to score 145,000 random web samples from the CCI3.0 dataset on a scale from 0(non-educational) to 5 (highly educational)
- The locally deployed API of Qwen2, integrated with vLLM [14], facilitates the annotation process. 
- Finally, we perform manual and GPT-4 evaluations on a subset of the labeled results, achieving an agreement rate exceeding 80%.