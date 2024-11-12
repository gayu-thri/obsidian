https://github.com/zama-ai/hf-blog/blob/zama-ai/encrypted-llm/evaluating-mmlu-leaderboard.md#now-how-do-we-evaluate-the-model-from-these-prompts

- MMLU is typically evaluated in 5 shots (prepending 5 examples to each prompt)
- To avoid the below scenarios (Correct, but not from the choices given in question)
	- ![[Pasted image 20241111172632.png]]
- MCQ on 57 tasks
- Type: Multi-choice
- Metric: Accuracy