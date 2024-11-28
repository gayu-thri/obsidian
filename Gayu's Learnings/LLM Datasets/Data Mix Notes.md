# Take-Aways
### In General
- Synthetic data, when carefully curated and integrated with publicly available high-quality datasets, can significantly enhance a model’s performance without requiring prohibitively large computational resources. [Ref in smoltalk](https://www.marktechpost.com/2024/11/21/smoltalk-released-the-dataset-recipe-behind-the-best-in-class-performance-of-smollm2/)
- Balanced mix of unstructured (*summary, text generation*) and structured (*text2code, text2sql*)
---
### Category - Data Mix
##### Text2CodeGeneration
- rombodawg/LosslessMegaCodeTrainingV3_Tiny
	- Dataset - ~80% coding instruction data and 20% non-coding instruction data
	- Amounting to 650,000 evol instruction-formatted lines of data.
	- 20% non coding instruction data - *preserves logic and reasoning skills within the model* while training on coding.[Ref](https://huggingface.co/datasets/rombodawg/LosslessMegaCodeTrainingV3_Tiny)
---
### Dataset - Data Mix

#### Cosmopedia
https://huggingface.co/datasets/HuggingFaceTB/cosmopedia
- Todo
#### Tulu3 SFT Mixture
https://huggingface.co/datasets/allenai/tulu-3-sft-mixture
https://allenai.org/papers/tulu-3-report.pdf
- ~1M (9,39,344 samples)
- Data mix
	- General
	- Knowledge Recall
	- Math reasoning
	- Coding
	- Safety & Non-compliance
	- Multilingual
	- Precise IF
	- ![[Pasted image 20241128191102.png]]
- Dataset composition
	- [CoCoNot](https://huggingface.co/datasets/allenai/coconot) (ODC-BY-1.0), 10,983 prompts
	- [FLAN v2](https://github.com/google-research/FLAN/tree/main) via [`ai2-adapt-dev/flan_v2_converted`](https://huggingface.co/datasets/ai2-adapt-dev/flan_v2_converted), 89,982 prompts
	- [No Robots](https://huggingface.co/datasets/HuggingFaceH4/no_robots) (CC-BY-NC-4.0), 9,500 prompts
	- [OpenAssistant Guanaco](https://huggingface.co/datasets/OpenAssistant/oasst1) (Apache 2.0), 7,132 prompts
	- [Tulu 3 Persona MATH](https://huggingface.co/datasets/allenai/tulu-3-personas-math) (ODC-BY-1.0), 149,960 prompts
	- [Tulu 3 Persona GSM](https://huggingface.co/datasets/allenai/tulu-3-sft-personas-math-grade) (ODC-BY-1.0), 49,980 prompts
	- [Tulu 3 Persona Python](https://huggingface.co/datasets/allenai/tulu-3-sft-personas-code) (ODC-BY-1.0), 34,999 prompts
	- [Tulu 3 Persona Algebra](https://huggingface.co/datasets/allenai/tulu-3-personas-algebra) (ODC-BY-1.0), 20,000 prompts
	- [Tulu 3 Persona IF](https://huggingface.co/datasets/allenai/tulu-3-sft-personas-instruction-following) (ODC-BY-1.0), 29,980 prompts
	- [NuminaMath-TIR](https://huggingface.co/datasets/AI-MO/NuminaMath-TIR) (CC-BY-NC-4.0), 64,312 prompts 
	- [Tulu 3 WildGuardMix](https://huggingface.co/datasets/allenai/wildguardmix) (Apache 2.0), 50,000 prompts
	- [Tulu 3 WildJailbreak](https://huggingface.co/datasets/allenai/wildjailbreak) (ODC-BY-1.0), 50,000 prompts
	- [Tulu 3 Hardcoded](https://huggingface.co/datasets/allenai/tulu-3-hard-coded) (CC-BY-4.0), 240 prompts
	- [Aya](https://huggingface.co/datasets/CohereForAI/aya_dataset) (Apache 2.0), 100,000 prompts
	- [WildChat GPT-4](https://huggingface.co/datasets/allenai/WildChat-1M) (ODC-BY-1.0), 100,000 prompts
	- [TableGPT](https://huggingface.co/datasets/LipengCS/Table-GPT) (MIT), 5,000 prompts
	- [SciRIFF](https://huggingface.co/datasets/allenai/SciRIFF) (ODC-BY-1.0), 10,000 prompts
	- [Evol CodeAlpaca](https://huggingface.co/datasets/theblackcat102/evol-codealpaca-v1) (Apache 2.0), 107,276 prompts
	
#### SmolLM corpus
https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus
- Dataset composition
	- Cosmopedia v2 - (28B tokens)
		- *synthetic textbooks & stories*
	- Python-Edu - (4B tokens)
		- *From "The Stack"*
	- FineWeb-Edu (220B tokens)
		- *deduplicated*
#### Smoltalk
https://huggingface.co/datasets/HuggingFaceTB/smoltalk
- 1M samples
- Dataset composition
	- New datasets
		- Smol-Magpie-Ultra - 400k (40%)
		- Smol-contraints - 36k (3.6%)
			-  *follow specific constraints, such as generating responses with a fixed number of sentences or words, or incorporating specified words in the output.*
		- Smol-rewrite - 50k (5%) (adjusting tone of writing to friendly/professional)
		- Smol-summarize - 100k (10%) (e-mail and news)
	- Existing datasets
		- *NOTE: To enhance capabilities in mathematics, coding, system prompts, and long-context understanding, we fine-tuned SmolLM2-1.7B on various public SFT datasets and included subsets of the best performing ones using tuned ratios*
		- [OpenHermes2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5) - 100k (10%)
			- *helps preserve & boost MMLU, WinoGrande and BBH*
		- [MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA?) - 50k random (5%)
			- *improve mathematics & reasoning*
		- [NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT)- 
			- *helps for hard problems in MATH benchmark*
		- [Self-Oss-Starcoder2-Instruct](https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2-exec-filter-50k) 
			- *improve coding capabilities*
		- [SystemChats2.0](https://huggingface.co/datasets/cognitivecomputations/SystemChat-2.0): 30k (3%)
			- *supports a variety of system prompt formats*
		- [LongAlign](https://huggingface.co/datasets/THUDM/LongAlign-10k):  english samples with <16k tokens & train with a 8192 sequence
			- *we find that finetuning model on only short samples makes it loose long context abilities beyond 2048 tokens*
		- [Everyday-conversations](https://huggingface.co/datasets/HuggingFaceTB/everyday-conversations-llama3.1-2k):
			- *multi-turn everyday conversations such as greeting*
			- *used in SmolLM v1 post-training*
		- [APIGen-Function-Calling](https://huggingface.co/datasets/argilla/apigen-function-calling): 80k (8%)
			- *(mix of [Synth-APIGen-v0.1](https://huggingface.co/datasets/argilla/Synth-APIGen-v0.1) and [xlam-function-calling-60k](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k) datasets)*
		- [Explore-Instruct-Rewriting](https://huggingface.co/datasets/Wanfq/Explore_Instruct_Rewriting_32k): 30k  (3%)

#### No Robots Dataset
- High quality SFT data
- Created by skilled human annotators
- 10k instructions
- Data mix summary
		Category	Count	Ratio
		==Generation==	4560	==45.6%==
		==Open QA==	1240	==12%==
		==Brainstorm==	1120	==11%==
		==Chat==	850	==8.5%==
		Rewrite	660	6.6%
		Summarize	420	4%
		Coding	350	3.5%
		Classify	350	3.5%
		Closed QA	260	2.6%
		Extract	190	1.9%
#### Llama 3 Dataset
https://arxiv.org/pdf/2407.21783
- Pre-training dataset data mix summary ( *Total = 15T multilingual tokens* )
	- 50% general knowledge tokens
	 - 25% mathematical and reasoning tokens
	 - 17% code tokens
	 - 8% multilingual tokens
 - SFT dataset data mix summary

| Dataset             | %OfExamples | Avg.#Turns | Avg.#Tokens | Avg.#TokensInContext | Avg.#TokensInFinalResponse |
| ------------------- | ----------- | ---------- | ----------- | -------------------- | -------------------------- |
| General-English     | ==52.66%==  | 6.3        | 974         | 656.7                | 317.1                      |
| Code                | ==14.89%==  | 2.7        | 753.3       | 378.8                | 374.5                      |
| Multilingual        | 3.01%       | 2.7        | 520.5       | 230.8                | 289.7                      |
| Exam-like           | ==8.14%==   | 2.3        | 297.8       | 124.4                | 173.4                      |
| Reasoning-and-tools | ==21.19%==  | 3.1        | 661.6       | 359.8                | 301.9                      |
| Long-context        | 0.11%       | 6.7        | 38,135.6    | 37,395.2             | 740.5                      |
| Total               | 100%        | 4.7        | 846.1       | 535.7                | 310.4                      |

#### Hermes 3 Dataset
https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1
- Total = 11k rows - 390M tokens
- Data mix summary

| Category               | Ratio   | Tokens (M) |
| ---------------------- | ------- | ---------- |
| ==General Instructions==   | ==60.6==    | ==236==        |
| Domain Expert          | 12.8    | 50         |
| Math                   | 6.7     | 26         |
| Roleplaying            | 6.1     | 24         |
| Coding                 | 4.5     | 18         |
| Tool Use, Agentic, RAG | 4.3     | 17         |
| Content Generation     | 3.0     | 12         |
| Steering and Alignment | 2.5     | 10         |
| **Total**              | **100** | **390**    |

- Total = **390M** tokens
	- Output = 69% (270M tokens) - *contributing to optimizer’s cross-entropy loss objective*
	- Input = 31% (120M tokens)
- For existing sources,
	- Datasets evaluated based on coherence, educational value, and reliability (236M tokens)
	- This process 
		- Contributed significantly to "General Instructions" category
		- Addressed known weakness in old Hermes models - Covered areas such as code, mathematics, roleplaying, agentics, and other miscellaneous domains
- Filtering techniques
	- Token length thresholds to balance conversation lengths
	- Removal of refusals and improperly formatted responses
	- Elimination of conversations with missing or empty turns
	- Prioritisation of conversations generated by the strongest models

---
