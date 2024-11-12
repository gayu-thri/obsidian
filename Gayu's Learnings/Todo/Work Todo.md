MMLU
https://docs.confident-ai.com/docs/benchmarks-mmlu
https://huggingface.co/meta-llama

MMLU Analysis:
- How the score MMLU is impacted by different datacut??
- What is the reason for MMLU score variations among different LLAMA versions??

>Yes, you can even download the code repo or model creation method of MMLU to see how it works if there are no resources. But need to find out how MMLU scores are impacted by a model.

---
**Nov 11, 2024**
- Go through this line by line  [https://github.com/hendrycks/test/pull/13](https://github.com/hendrycks/test/pull/13)
**Nov 12, 2024**
- MMLU Analysis
	- Reason for scores variations
	- If data in benchmark and training overlaps??
	- How are they evaluating??
- Half day to check if this can be adapted
	- https://docs.dask.org/en/stable/gpu.html
	- https://www.zyphra.com/post/building-zyda-2
---

Training overview:
- Llama 3 paper for overview
- https://huggingface.co/NousResearch/Llama-2-7b-chat-hf
DPO  
Architectures used for LLMs  
- [https://www.labellerr.com/blog/exploring-architectures-and-configurations-for-large-language-models-llms/amp/](https://www.labellerr.com/blog/exploring-architectures-and-configurations-for-large-language-models-llms/amp/)  
- [https://whylabs.ai/learning-center/introduction-to-llms/understanding-large-language-model-architectures](https://whylabs.ai/learning-center/introduction-to-llms/understanding-large-language-model-architectures)  
Floating point operations (FLoPs)  
Mixed precision (fp16, fp32)  
Optimiser (Adam, Adafactor)  
RoPE  
SwiGLU activation function  
Gradient checkpoints  
  
Code  
- Fine-tuning BERT or GPT-like models (HuggingFace NLP Course)  
- [https://huggingface.co/learn/nlp-course/en/chapter7/6](https://huggingface.co/learn/nlp-course/en/chapter7/6)  
- [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)(Edited)

