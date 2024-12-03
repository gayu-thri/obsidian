LLM
- Normalization 
	- LLMs commonly use "*RMS Norm*"
	- ***READ***: Batch Norm vs Layer Norm vs RMS Norm VS Deep Norm
- Activation Functions
	- LLMs commonly use *"GeLU"*
	- ***READ***: GeLU vs [SwiGLU](https://paperswithcode.com/method/swiglu?ref=labellerr.com) vs GeGLU
- Positional Embeddings
	- LLMs commonly use "*RoPE*"
	- Vanilla Transformer has two absolute position embeddings: sinusoids & learned position embeddings
	- LLMs commonly utilize "*Learned Position Embeddings*"
	- Relative positional encodings 
		- Generate embeddings based on the offsets between keys and queries
		- Allows to perform well on longer sequences - even ones beyond the lengths encountered during training, *enabling extrapolation*.
	- [ALiBi](https://www.seldon.io/solutions/open-source-projects/alibi-explain?ref=labellerr.com) 
		- Introduces penalty based on distance between keys and queries
		- To bias attention scores
		- Resulting in better [zero-shot generalization](https://towardsdatascience.com/understanding-zero-shot-learning-making-ml-more-human-4653ac35ccab?ref=labellerr.com) & stronger extrapolation capabilities than other position embeddings
	- [RoPE](https://arxiv.org/pdf/2104.09864.pdf?ref=labellerr.com)
		- uses rotatory matrices based on absolute positions to compute scores between keys and queries
		- incorporating relative position information for modeling long sequences. 
		- Recent LLMs widely adopt RoPE as a consequence of its benefits.

![Positional Embedding](https://cdn.labellerr.com/language%20models-4/PE1-1024x545.webp)

***READ BELOW (TODO)***
### Attention and Bias

In addition to the full self-attention mechanism in the original Transformer, GPT-3 utilizes sparse attention, specifically [Factorized Attention](https://paperswithcode.com/method/fixed-factorized-attention?ref=labellerr.com), to reduce computation complexity.

Researchers explore various approaches to effectively model longer sequences, including introducing special attention patterns or optimizing GPU memory access, as seen in models like [FlashAttention.](https://arxiv.org/abs/2205.14135?ref=labellerr.com)

Moreover, while biases are typically included in each dense kernel and [Layer Norm](https://pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html?ref=labellerr.com) following the original Transformer, recent LLMs like PaLM and [Galactica](https://arxiv.org/abs/2211.09085?ref=labellerr.com) have removed biases. Removing biases improves training stability in LLMs, as demonstrated in studies.

![Detailed formulations for the network configurations.](https://cdn.labellerr.com/language%20models-4/Screenshot%202023-05-21%20233405.webp)Detailed formulations for the network configurations.

**Figure 4**: Detailed formulations for the network configurations.

To summarize the suggestions from existing literature regarding detailed configuration for Language Models (LLMs): for stronger generalization and training stability, it is recommended to use [pre-RMS Norm](https://arxiv.org/abs/1910.07467?ref=labellerr.com) for layer normalization and SwiGLU or GeGLU as the activation function.

It is advised not to use LN immediately after embedding layers as it may lead to performance degradation.

Regarding position embeddings, RoPE or ALiBi is a better choice as they perform well on long sequences.

## Conclusion

Large language models (LLMs) have changed how we solve natural language tasks, thanks to improvements in their design and training methods. Key advancements like better model architectures, smarter attention mechanisms, and efficient training techniques are shaping the future of AI.

What do you think will be the next big breakthrough in LLMs?

As these models improve, areas like handling long sequences and making them more efficient will remain important.

For more in-depth articles and the latest insights on large language models, check out the [LLM Blog Series](https://www.labellerr.com/blog/tag/large-language-models/).

### Frequently Asked Questions (FAQ)

**1. What are large language models (LLMs)?**

Large language models (LLMs) are powerful artificial intelligence models that excel in natural language processing tasks. They are trained on vast amounts of text data and have shown remarkable capabilities in tasks like text generation, language translation, and question-answering.

**2. How do LLMs contribute to advancements in AI and NLP?**

LLMs have opened up new possibilities in AI and NLP applications. They have improved chatbots, automated content generation, and voice assistants. LLMs have also enhanced various NLP tasks, enabling more accurate language understanding and generation.

**3. What are the different types of LLM architectures?**

LLM architectures can be broadly classified into three types: encoder-decoder, causal decoder, and prefix decoder. Each type has its own advantages and has been used in different LLM models for specific purposes.

**4. Which activation functions are commonly used in LLMs?**

GeLU (Gaussian Error Linear Unit) activations are commonly used in existing LLMs. However, recent models like PaLM and LaMDA have employed variants of GLU (Gated Linear Unit) activation, such as SwiGLU and GeGLU, which have shown better performance in practical applications.