https://whylabs.ai/learning-center/introduction-to-llms/understanding-large-language-model-architectures
https://huggingface.co/blog/moe?ref=content.whylabs.ai
https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts

- 4 types
	- Encoder-decoder
	- Encoder-only
	- Decoder-only
	- Mixture of experts (MoE)
- Not all LLMs are Transformer-based models
- MoE - Large LLMs -> breaks to smaller “expert” models
	- Diverse skill sets that are better at handling specialised tasks
	- SCALE & PERFORM BETTER without computational bottlenecks.
---
====================
#### *ENCODER-DECODER*
====================
- **Encoder** 
	- Accepts input data and converts it into an abstract continuous representation
	- Captures the main characteristics of the input
- **Decoder**
	- Translates continuous representation into intelligible outputs
	- Ingests previous outputs
- ![[Pasted image 20241108100833.png]]

- Handle complex language tasks - efficient representation of the data - helping model's coherence response
- Use cases
	- ==GENERATIVE TASKS==
	- Machine translation (converting the same sentence from one language to another) and text summarization (summarizing the same key points in the text)
	- Wherever *==comprehending the entire input before generating output==* is crucial
- ==SLOWER IN INFERENCE== *(as it needs to process the holistic input first)*

**LLM examples:**
	- Google’s - [T5](https://blog.research.google/2020/02/exploring-transfer-learning-with-t5.html?ref=content.whylabs.ai), [Flan-UL2](https://huggingface.co/google/flan-ul2?ref=content.whylabs.ai), and [Flan-T5](https://paperswithcode.com/method/flan-t5?ref=content.whylabs.ai).
	- Meta’s [BART](https://research.facebook.com/publications/bart-denoising-sequence-to-sequence-pre-training-for-natural-language-generation-translation-and-comprehension/?ref=content.whylabs.ai).

----
*====================
#### ENCODER-ONLY
====================
- BERT & RoBERTa - encoder only architectures
- Input -> input into rich, contextualised representations without directly generating new sequences
- BERT 
	- Pre-trained on extensive text corpora using two innovative approaches: 
		- Masked language modelling (MLM)
		- Next-sentence prediction
	- ![[Pasted image 20241108101823.png]]
- Masked LM
	- ==*Hiding random tokens in input*== & training model to ==*predict these tokens from their context.*== 
	- In this way, model understands relationship between both left and right contexts.
	- This *==“bidirectional” understanding==* - crucial for tasks requiring strong language understanding, such as sentence classification (e.g., sentiment analysis) or fill missing words.

> Unlike encoder-decoder models that can interpret and generate text, ==encoder-only don't natively generate long text sequences==. They focus more on interpreting input.

**LLM examples:**

- Google’s [BERT](https://research.google/pubs/bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding/?ref=content.whylabs.ai) and [ALBERT](https://blog.research.google/2019/12/albert-lite-bert-for-self-supervised.html?ref=content.whylabs.ai).
- Meta’s [RoBERTa](https://ai.meta.com/blog/roberta-an-optimized-method-for-pretraining-self-supervised-nlp-systems/?ref=content.whylabs.ai).
- Microsoft’s [DeBERTa](https://github.com/microsoft/DeBERTa?ref=content.whylabs.ai).

---
*====================
#### DECODER-ONLY
====================

---
*====================
#### MoE
====================
- Adopted by models like Mistral 8x7B
- Diverges from traditional Transformer models
- Single monolithic language model -> smaller, specialized sub-models
- ==*REPLACES **DENSE FFN LAYER -> SPARSE SWITCH FFN LAYER (MoE)***==
- ![[Pasted image 20241108122001.png]]
- https://huggingface.co/blog/moe?ref=content.whylabs.ai
- Pros & Cons
	- Pros
		- ==Compute-efficient pre-training==
		- Only some parameters are used during inference -> ==*FASTER INFERENCE*==
	- Cons
		- Hard to generalize during fine-tuning -> ==*Overfitting*==
		- All parameters loaded in RAM -> ==*Higher memory requirements*==
		- Mixtral 8 x 7 B
			- VRAM should hold dense 47B parameters
			- Why not 56B?
			- in MoE models -> FFN layers are individual experts
- MoE has 2 main elements:
	- **SPARSE MoE LAYERS**
		- Instead of dense FFN layers
		- Certain number of experts, ex: 8 
		- Expert = NN / FFN / Complex networks / MoE itself
	- **GATE NETWORK (OR) ROUTER**
		- Decides which tokens sent to which expert
		- ![[Pasted image 20241108123402.png]]
		- In example,
			- "more" -> 2nd expert
			- "parameters" -> 1st network
		- 1 token -> Many experts (*possible*)
		- How to route?? 
			- -> Router - learned parameters; pretrained at same time as rest of network
https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts
