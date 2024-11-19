### Feasibility of Dask Integration in Data Tool

##### Bookmarks
https://docs.dask.org/en/stable/10-minutes-to-dask.html
Check how it's being used in NeMo Curator (https://www.zyphra.com/post/building-zyda-2)
NeMo Dask usage code link
Feasibility of integration in each module
Data Loading: 
With `load_dataset()` and `Dataset` object, there seems to be no support for speed up
However, it has alternate methods and formats
Dataframe (like .from_csv() - More here) 
Bag (Creation of bags)
Array (Do not have loading data from a file as such)
Data Tokenisation:
Dask can be integrated if following,
out-of-memory large datasets
Dataset is too large to fit into memory & want to process it in chunks
Cons side of using Dask
Conversion Time
Converting dataset to a Dask supported dtype
Steps
Convert `Dataset` -> `DataFrame`
Tokenize operations
Convert back `DataFrame` -> `Datasets`
Running Filters & Meta Ingestion:
Todo
Recipe Generation:
Todo
Keyword Search:
Todo

### Code snippet that was tried for each module
Data Tokenisation:
```python
import dask.dataframe as dd
from transformers import AutoTokenizer
from datasets import load_dataset
from multiprocessing import Value
from datasets import Dataset

# Load the data
dataset = load_dataset(
 "imdb",
 split="train",
 cache_dir="/data1/gayu/hf_cache"
)

def filter_na_in_data(input_text: str) -> bool:
 """
 Filters the data based on the column name and returns
 boolean value based on the presence of NA values.
 """
 nan_possibilities = ["", str(None), None, "NaN"]
 return input_text not in nan_possibilities
def filter_and_tokenize_with_dask(dataset, field, tokenizer_path, batch_size):
 # Load the tokenizer
 tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
 
 # Convert dataset to a Dask DataFrame
 df = dd.from_pandas(dataset.to_pandas(), npartitions=4) # Adjust npartitions as needed
 
 # Filter NA values using Dask
 filtered_df = df[df[field].map(filter_na_in_data, meta=(field, 'bool'))]
 
 # Tokenize the filtered data
 def tokenize_partition(partition):
 """
 Tokenizes the partition and adds metadata for each row.
 """
 max_length = tokenizer.model_max_length # Get the model's max length
 partition["tokenized_list"] = partition[field].apply(
 lambda x: tokenizer.tokenize(x, add_special_tokens=True, max_length=max_length, truncation=True)
 if isinstance(x, str)
 else []
 )
 partition["tokenized_list_len"] = partition["tokenized_list"].apply(len)
 partition["text_len"] = partition[field].apply(len)
 return partition
 
 # Update meta to match the actual column order
 meta = {
 field: "str",
 "label": "object", # Ensure this comes before the additional columns
 "tokenized_list": "object",
 "tokenized_list_len": "int",
 "text_len": "int"
 }
 
 tokenized_df = filtered_df.map_partitions(tokenize_partition, meta=meta)
 
 # Reorder columns explicitly to match `meta`
 tokenized_df = tokenized_df[["text", "label", "tokenized_list", "tokenized_list_len", "text_len"]]
 
 # Debugging step: Inspect tokenized_df
 print("Tokenized DataFrame Sample:", tokenized_df.head())
 
 # Compute aggregated counts
 tokens_count = tokenized_df["tokenized_list_len"].sum().compute()
 filtered_rows_count = len(df) - len(filtered_df)
 
 # Convert back to Hugging Face Dataset if needed
 tokenized_data = Dataset.from_pandas(tokenized_df.compute())
 
 return tokenized_data, tokens_count, filtered_rows_count

# Example usage
tokenized_dataset, tokens_count, filtered_rows_count = filter_and_tokenize_with_dask(
 dataset=dataset,
 field="text",
 tokenizer_path="bert-base-uncased",
 batch_size=64,
)

print(f"Tokens Count: {tokens_count}")
print(f"Filtered Rows Count: {filtered_rows_count}")
```

