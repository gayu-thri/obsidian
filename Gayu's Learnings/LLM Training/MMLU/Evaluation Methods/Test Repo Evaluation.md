
STEPS
- Load model 
	- `AutoModelForCausalLM.from_pretrained()` & `torch_dtype=torch.float16`
- Set model in evaluation mode by default 
	- `model.eval()` (Dropout modules are deactivated)
- Load tokenizer
	- `AutoTokenizer.from_pretrained()`
- Custom ***eval()*** method
	- Create the prompt with n-shots (0/5) - Train prompt + Question prompt
		- Train prompt starts with
			```python
					prompt = "The following are multiple choice questions (with answers) about {}.\n\n".format(
		        format_subject(subject)
				    )
			```

	- Tokenize prompt - Get input_ids
	- Get gold label
		- `label = test_df.iloc[i, test_df.shape[1] - 1]`
	- Get pred label
		- `logits = model(input_ids=input_ids).logits[0, -1]`
		- `logits[0, -1]` gives the logits for the last position in the sequence
		- Last idx often assumed to be the best indicator for the next token prediction.
	- Get probabilities of each choice
		```python
		probs = (
            torch.nn.functional.softmax(
                torch.tensor(
                    [
                        logits[tokenizer("A").input_ids[-1]],
                        logits[tokenizer("B").input_ids[-1]],
                        logits[tokenizer("C").input_ids[-1]],
                        logits[tokenizer("D").input_ids[-1]],
                    ]
                ).float(),
                dim=0,
            )
            .detach()
            .cpu()
            .numpy()
        )
		```

		- Logits -> probabilities *(using a softmax function)*
		- Each value (0-1) & they sum up to 1 (*normalizing*)
		- Gives likelihood of each option being the correct answer
	- Predict the label
		- `pred = {0: "A", 1: "B", 2: "C", 3: "D"}[np.argmax(probs)]`
		- `np.argmax(probs)` - index of the highest probability, which is then mapped to the corresponding label using a dictionary.
	- Compare pred with gold label
		```python
			cor = pred == label
		    cors.append(cor)
		        all_probs.append(probs)
		
		    acc = np.mean(cors)
		    cors = np.array(cors)
		
		    all_probs = np.array(all_probs)
		    print("Average accuracy {:.3f} - {}".format(acc, subject))
		```