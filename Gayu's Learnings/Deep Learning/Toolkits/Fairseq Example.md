## prepare_txt_dataset.py
```python
from datasets import load_dataset

from transformers import AutoTokenizer

from multiprocessing import Value

  

tokens_count = Value("l", 0) # Handling value for multiple processor

  

data = load_dataset(

"knkarthick/dialogsum",

split="train[:100]",

cache_dir="/home/gayu/hf_cache",

num_proc=8,

)

  

val_data = load_dataset(

"knkarthick/dialogsum",

split="validation[:20]",

cache_dir="/home/gayu/hf_cache",

num_proc=8,

)

  

"""

Dataset({

features: ['id', 'dialogue', 'summary', 'topic'],

num_rows: 100

})

"""

  

# Tokenize the field "summary"

  

def tokenize_function(tokenizer, example, field="text"):

"""

This function takes care of tokenizing the data and adding necessary meta data.

"""

tokenized_text = tokenizer.tokenize(example[field], add_special_tokens=True)

tokenized_text_len = len(tokenized_text)

example["text_len"] = len(example[field])

example["tokenized_list_len"] = tokenized_text_len

example["tokenized_list"] = tokenized_text

with tokens_count.get_lock():

tokens_count.value += tokenized_text_len

return example

  

tokenizer = AutoTokenizer.from_pretrained(

"/home/gayu/workspace/dev/dataops/meerkat_tokenizer/src/meerkat_v3"

)

tokenized_dataset = data.map(

lambda example: tokenize_function(tokenizer, example, field="summary"),

num_proc=64

)

print("Total token count: ", tokens_count.value)

  

tokens_count.value = 0

val_tokenized_dataset = val_data.map(

lambda example: tokenize_function(tokenizer, example, field="summary"),

num_proc=64

)

print("Total token count: ", tokens_count.value)

  

with open("/home/gayu/workspace/dev/slurm_setup/data/recipe.txt", "w") as fp:

for tokenized_list in tokenized_dataset["tokenized_list"]:

tokenized_string = " ".join(tokenized_list)

fp.write(f"{tokenized_string}\n")

  

with open("/home/gayu/workspace/dev/slurm_setup/data/val_recipe.txt", "w") as fp:

for tokenized_list in tokenized_dataset["tokenized_list"]:

tokenized_string = " ".join(tokenized_list)

fp.write(f"{tokenized_string}\n")
```


## fairseq-preprocess
```bash
# Preprocess/binarize the data

fairseq-preprocess \

--trainpref data/recipe.txt \

--validpref data/val_recipe.txt \

--only-source \

--destdir data-bin/dialogsum \

--workers 20 \
```

## fairseq-train
```bash
# Change according to SLURM setup; Use `scrun`;

CUDA_VISIBLE_DEVICES=4 fairseq-train \

data-bin/dialogsum \

--task language_modeling \

--save-dir checkpoints/dialogsum \

--arch transformer_lm \

--share-decoder-input-output-embed \

--dropout 0.1 \

--optimizer adam \

--adam-betas '(0.9, 0.98)' \

--weight-decay 0.01 \

--clip-norm 0.0 \

--lr 0.0005 \

--lr-scheduler inverse_sqrt \

--warmup-updates 4000 \

--warmup-init-lr 1e-07 \

--tokens-per-sample 512 \

--sample-break-mode none \

--max-tokens 2048 \

--update-freq 16 \

--fp16 \

--max-update 50000 \
```