
---
##### *Generic Info On MMLU*
- Massive Multitask Language Understanding (MMLU)
- Tests *==zero-shot & few-shots understanding==* (General knowledge of a model)
- MMLU 0-shot evalutation
	- Tasks it has never seen before - No specific examples / training data
- MMLU 5-shot evaluation
	- 5 example problems + Ask to solve additional one
	- Tests this -> How well model can generalise from small amount of task-specific info
- MMLU
	- Has questions across 57 subjects - astronomy, biology, micro-ecnomics, etc..
	- Broad spectrum of human knowledge

>*The LLM is scored based on the percentage of questions it gets correct.*

---
### *In Paper*
- ==All are Llama 3.1==
	- "All the results presented in this paper are for the Llama 3.1 models"
- **==Llama 3 = Llama 3.1==** 
	- "which we will refer to as Llama 3 throughout for brevity."
- MMLU - To evaluate Llama 3’s capability on ==*knowledge-based question answering.*==
- Paper provide ==**only aggregate MMLU scores**==
	- No exact scores for each subtask
- ***==3.2 not mentioned*** in paper anywhere==
- Llama versions & sizes
	- https://github.com/meta-llama/llama-models/tree/main
	- Llama 3: 8B, 70B (https://ai.meta.com/blog/meta-llama-3/)
	- Llama 3.1: 8B, 70B, 405B (https://ai.meta.com/blog/meta-llama-3-1/)
	- Llama 3.2: 1B, 3B, 11B, 90B (https://www.llama.com/)
