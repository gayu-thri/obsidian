-> **MMLU GitHub Pull request code**: https://github.com/hendrycks/test/blob/461a38863ce51d29f657a92c6b90be501be53fc5/evaluate_hf.py | https://github.com/hendrycks/test/pull/13
 - load models as Float16;
- put the samples on the same device as a model;
- use the last token of option tokenization instead of the first one;
- save the aggregated results to a JSON file.

-> **DeepEval code**: https://docs.confident-ai.com/docs/benchmarks-introduction#benchmarking-your-llm
-> **OpenNMT code**: https://github.com/OpenNMT/OpenNMT-py/blob/master/eval_llm/MMLU/run_mmlu_opennmt.py

-> **HuggingFace code**:
```python
# pip install torch transformers datasets
from datasets import load_dataset
from transformers import pipeline

mmlu_subset = "elementary_mathematics"  # "all" for all the subsets
mmlu = load_dataset("cais/mmlu", mmlu_subset, cache_dir="/data1/gayu/hf_cache")

"""
================================================================================
Example for Llama 3 (update model name as needed for 3.1 and 3.2)
================================================================================
# 3     :: unsloth/Meta-Llama-3.1-8B    |   "meta-llama/Meta-Llama-3-8B"    (no access)
# 3.1   :: unsloth/llama-3-8b           |   "meta-llama/Llama-3.1-8B"       (no access)
# 3.2   :: NOTE: No 8B in Llama 3.2
================================================================================
"""

model_name = "unsloth/llama-3-8b "  # Replace with actual names of the Llama 3, 3.1, 3.2 models

# Load pipeline for zero-shot classification
nlp_pipeline = pipeline(
    "text-generation",
    model=model_name,
    tokenizer=model_name,
    device=6,
)

correct, total = 0, 0

for item in mmlu["test"]:
    question = item["question"]
    choices = item["choices"]
    answer = item["answer"]

    # Generate answer
    response = nlp_pipeline(question + "\n" + " ".join(choices))

    print(f"Question: {question}\nResponse: {response}\n")
    print("=" * 50)
    # Compare response to the correct answer
    if response.strip() == answer.strip():
        correct += 1
    total += 1

accuracy = correct / total
print(f"Accuracy on MMLU: {accuracy * 100:.2f}%")

```