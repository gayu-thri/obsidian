### LLama 3 8b Instruct
- instruction tuned text only models are optimised for 
	- *==dialogue use cases==*
	- *==helpfulness==* and *==safety==*

##### Model specifics
- 2 sizes:  8B & 70B parameters
- Input & output
	- I/P: Text only
	- O/P: Text & code only
- Auto-regressive language model
- Optimized transformer architecture
- SFT and RLHF to align with human preferences
- Context length = **8k**
- Uses Grouped-Query Attention (GQA) - for inference stability

##### Training data
- Pre-trained
	- *15 trillion tokens of data*
	- From publicly available sources
	- Cutoff of March 2023 for 8B
- Fine-tuning
	- From publicly available instruction datasets
	- Over 10M human-annotated examples

---
### LLama 3.1 8b Instruct
- Instruction tuned text only models are optimised for 
	- *==**Multilingual** dialogue use cases==*
- **Supported languages:** 
	- English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai.
##### Model specifics
- 2 sizes:  8B, 70B & 405B parameters
- Input & output
	- I/P: Text only
	- O/P: Text & code only
- Auto-regressive language model
- Optimized transformer architecture
- SFT and RLHF to align with human preferences
- Context length = **128k**
- Uses Grouped-Query Attention (GQA) - for inference stability

##### Training data
- Pre-trained
	- ~*15 trillion tokens of data*
	- From publicly available sources
	- cutoff of December 2023
- Fine-tuning
	- From publicly available instruction datasets
	- 25M synthetically generated examples
- Multi-faceted approach to data collection
	- **Combining human-generated data** from our vendors **with synthetic data**
		- to mitigate potential safety risks
	- Developed many ***LLM-based classifiers***
		- to thoughtfully select high-quality prompts and responses, enhancing data quality control.
---
### LLama 3.2 11b Vision Instruct
