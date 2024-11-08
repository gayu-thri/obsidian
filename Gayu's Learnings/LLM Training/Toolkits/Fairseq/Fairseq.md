- https://fairseq.readthedocs.io/en/latest/command_line_tools.html
- **Example of translation using fairseq**
	- https://github.com/facebookresearch/fairseq/blob/main/examples/translation/README.md

- **CLI Tools for training & evaluating models**
	- [fairseq-preprocess](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#fairseq-preprocess): Data pre-processing: build vocabularies (.idx) and binarize (.bin) training data
	- [fairseq-train](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#fairseq-train): Train a new model on one or multiple GPUs
	- [fairseq-generate](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#fairseq-generate): Translate pre-processed data with a trained model
	- [fairseq-interactive](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#fairseq-interactive): Translate raw text with a trained model
	- [fairseq-score](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#fairseq-score): BLEU scoring of generated translations against reference translations
	- [fairseq-eval-lm](https://fairseq.readthedocs.io/en/latest/command_line_tools.html#fairseq-eval-lm): Language model evaluation

| Input files                                    | Command            | Output files                                   |
| ---------------------------------------------- | ------------------ | ---------------------------------------------- |
| train.txt & valid.txt                          | fairseq-preprocess | train.bin & valid.bin<br>train.idx & valid.idx |
| train.bin & valid.bin<br>train.idx & valid.idx | fairseq-train      |                                                |
|                                                |                    |                                                |
### fairseq-preprocess
- Bin and idx (vocab) files are generated 
	- ![[Pasted image 20240531134155.png]]
- 