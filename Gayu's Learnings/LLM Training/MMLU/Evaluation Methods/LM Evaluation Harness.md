https://github.com/EleutherAI/lm-evaluation-harness
- Almost similar to Test Repo evaluation
###### NOTES
- "You can expect results to vary slightly for different batch sizes because of padding."  
	- [Source Open LLM Leaderboard - About section](https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard)
  > Batch size I used = 8

###### STEPS
- Calculating accuracy
```python
class MultipleChoiceTask(Task):
	...
	def process_results(self, doc: dict, results: Iterable[Tuple[float, bool]]) -> dict:
        results = [
            res[0] for res in results
        ]  # only retain loglikelihoods, discard is_greedy TODO: do we need is_greedy anywhere?
        gold = doc["gold"]

        acc = 1.0 if np.argmax(results) == gold else 0.0
        completion_len = np.array([float(len(i)) for i in doc["choices"]])
        acc_norm = 1.0 if np.argmax(results / completion_len) == gold else 0.0

        return {
            "acc": acc,
            "acc_norm": acc_norm,
        }
```
- 