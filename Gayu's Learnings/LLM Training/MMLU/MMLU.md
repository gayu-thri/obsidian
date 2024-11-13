https://github.com/zama-ai/hf-blog/blob/zama-ai/encrypted-llm/evaluating-mmlu-leaderboard.md#now-how-do-we-evaluate-the-model-from-these-prompts

### INTRO
- MMLU is typically evaluated in 5 shots (prepending 5 examples to each prompt)
- To avoid the below scenarios (Correct, but not from the choices given in question)
	- ![[Pasted image 20241111172632.png]]
- MCQ on 57 subjects
	- Type: Multi-choice
	- Metric: Accuracy
	- Few-shots: 0 and 5
- Tests both ***world knowledge*** and ***problem solving ability***.
- Includes both easy & difficult QA
	- School subjects
	- Wide range of difficult subjects that go far beyond linguistic understanding

### SOURCES
- The questions in dataset
	- Manually collected by graduate & undergraduate students from online
- include practice questions for tests such as
	- ***GRE
	- ***United States Medical Licensing Examination*** - *“Professional Medicine”*
- questions designed for ***undergraduate courses***
- questions designed for readers of ***Oxford University Press books***
- Some tasks cover subject like ***Psychology***
	- ***Examination for Professional Practice in Psychology*** - *"Professional psychology"*
	- ***Advanced Placement Psychology examinations.*** - *“High School Psychology”*
- Explicit datasets mentioned in paper
	- ***ETHICS*** dataset - "*moral_scenarios*"
	- harder version of the physical commonsense benchmark ***Physical IQA*** - "*physics*"

### LLAMA SOURCES
Taken from "Data mix summary" in paper
 - 50% general knowledge tokens
 - 25% mathematical and reasoning tokens
 - 17% code tokens
 - 8% multilingual tokens
 
### GPT-3 Evaluation Insights in MMLU Paper
- Declarative knowledge >>> Procedural knowledge
- Knows PEMDAS, but not consistently applying
- . GPT-3 does better on College Medicine (47.4%)
and College Mathematics (35.0%) than calculation-heavy Elementary Mathematics (29.9%)

- Models are poor 
	- at modeling human (dis)approval
	- Professional Law
	- Moral Scenarios tasks
	- Have difficulty performing calculations
	- Elementary Mathematics
	- other STEM subjects with “plug and chug” problems