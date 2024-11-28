## References
1. Tulu3 - [Link](https://huggingface.co/datasets/allenai/tulu-3-sft-mixture)
2. WizardLMTeam/WizardLM_evol_instruct_70k - [Link](https://huggingface.co/datasets/WizardLMTeam/WizardLM_evol_instruct_70k)
3. smoltalk - [Link](https://huggingface.co/datasets/HuggingFaceTB/smoltalk)
4. HuggingFaceTB/smollm-corpus - [Link](https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus)
5. HuggingFaceTB/cosmopedia - [Link](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia)
## Blogs
- https://www.amd.com/en/developer/resources/technical-articles/introducing-the-first-amd-1b-language-model.html
	1. **Phase 1:** First, we fine-tune the model on [TuluV2](https://huggingface.co/datasets/allenai/tulu-v2-sft-mixture) dataset, which is a publicly available high-quality instruction dataset consisting of 0.66 billion tokens.
	2. **Phase 2:** To further improve the instruction following capabilities, we subject the model to be fine-tuned on a relatively larger instruction dataset [OpenHermes 2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5). In this phase, we also use [Code-Feedback](https://huggingface.co/datasets/m-a-p/Code-Feedback) and [WebInstructSub](https://huggingface.co/datasets/TIGER-Lab/WebInstructSub) dataset to improve the model’s capability along the dimensions of coding, science and mathematical problem solving.  These datasets consist of ~7 billion tokens in total.
## ChatGPT output

If you're looking for a unified dataset that covers multiple domains and tasks like summarization, text-to-structure generation (e.g., SQL, code), QA, and classification, a few datasets or projects are specifically designed to provide such broad coverage. Here are some potential alternatives to the OpenHermes dataset:

---

### **1. Dolly 15K**

#### **Details**

- **Tasks Covered**: Summarization, in-context QA, text-to-code, text-to-structural generation (like SQL), classification, and text generation.
- **Data Mix**: Curated through instruction-tuning approaches, with datasets designed for diverse tasks by crowdsourcing responses from high-quality workers.
- **Why This Mix?** It ensures high-quality responses across multiple domains while maintaining consistency and task diversity.

#### **Advantages**:

- Explicitly built for instruction-tuning LLMs.
- Wide coverage of tasks with real-world relevance.

#### **Limitations**:

- Primarily instruction-tuned; might lack depth in specialized domains like code or SQL.

---

### **2. FLAN (Fine-tuned Language Net)**

#### **Details**

- **Tasks Covered**: Summarization, classification, in-context QA, text-to-structure (SQL, code generation), and text generation.
- **Data Mix**: Aggregates datasets across multiple NLP benchmarks, including:
    - **SuperGLUE**: QA and classification.
    - **CodeXGLUE**: Code and unit test generation.
    - **Natural Questions**: In-context QA.
    - **MS MARCO**: Text-to-structural tasks (like SQL).
    - **XSum**: Summarization.
- **Why This Mix?** FLAN's goal is to generalize to multiple downstream tasks by fine-tuning on instruction-style prompts, ensuring cross-domain robustness.

#### **Advantages**:

- A rich mixture of tasks in a single fine-tuning framework.
- Already optimized for prompt-based generation.

#### **Limitations**:

- May not emphasize specific domains like complex SQL or unit test generation.

---

### **3. BigScience BLOOM-Finetune**

#### **Details**

- **Tasks Covered**: Summarization, text-to-structural (SQL), text-to-code, QA, classification, text generation.
- **Data Mix**: Leverages diverse multilingual and multi-domain datasets, such as:
    - **The Pile**: General-purpose text generation.
    - **Spider**: Text-to-SQL.
    - **CodeSearchNet**: Code-related tasks (unit test generation, code completion).
    - **OpenQA benchmarks**: QA and summarization.
- **Why This Mix?** It emphasizes creating a balanced representation of structured and unstructured tasks while being multilingual and inclusive.

#### **Advantages**:

- Extremely broad coverage.
- Includes multi-domain and multi-lingual datasets.

#### **Limitations**:

- May require preprocessing and filtering to align with specific needs.

---

### **4. CodeT5+ Pretraining Dataset**

#### **Details**

- **Tasks Covered**: Text-to-structural generation (SQL, code), code summarization, unit test generation, classification, and text generation.
- **Data Mix**:
    - Combines **CodeXGLUE** (unit tests, summarization) with **NL2SQL** and datasets like **Spider** (SQL).
    - Includes general NLP benchmarks for summarization (e.g., XSum) and classification (e.g., SST).
- **Why This Mix?** Balances domain-specific tasks (code-related) with general NLP, making it an excellent choice for both code and natural language tasks.

#### **Advantages**:

- Strong focus on code-related tasks.
- Effective for multitask settings involving SQL and unit test generation.

#### **Limitations**:

- Heavily code-oriented, which might dilute focus on other NLP domains.

---

### **5. OpenAssistant Conversations Dataset (OASST1)**

#### **Details**

- **Tasks Covered**: Text-to-structural generation, text-to-code, summarization, classification, QA, and text generation.
- **Data Mix**: Contains multi-turn conversation data created with user instructions and responses.
- **Why This Mix?** It's crowdsourced with specific task prompts that span multiple domains, ensuring task variety and instructional depth.

#### **Advantages**:

- Designed to replicate real-world interactions.
- Rich and diverse instructions for fine-tuning.

#### **Limitations**:

- May require additional curation for structured tasks like SQL.

---

### **Choosing the Right Dataset**

When deciding on the dataset:

1. **Task Balance**: Ensure it contains a balanced mix of unstructured (summarization, text generation) and structured (text-to-SQL, code) tasks.
2. **Quality**: Look for datasets with high-quality labels (e.g., FLAN, Dolly 15K).
3. **Data Diversity**: Prioritize datasets that span multiple domains and formats for generalization.

Let me know which tasks you want the dataset to emphasize, and I can refine the recommendation further!