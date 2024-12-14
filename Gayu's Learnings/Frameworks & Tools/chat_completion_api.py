import argparse
import json
import re
import time
from multiprocessing import Manager, Process
from multiprocessing.queues import Queue
from typing import List, Tuple

import openai
import tiktoken
from joblib import Parallel, delayed
from tenacity import stop_after_attempt  # for exponential backoff
from tenacity import retry, wait_random_exponential
from tqdm import tqdm
from zspeech.preprocessing.utils import clean_and_verify_transcript

# Authentication using the API key in Vault
openai.api_key = ""

# Choose a model ID & encoding for it
ROLE = "user"
MODEL_ID = "gpt-3.5-turbo"  # Max tokens 4,096 (inclusive of I/P & O/P)
ENCODING = tiktoken.get_encoding("cl100k_base")


def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    num_tokens = len(ENCODING.encode(string))
    return num_tokens


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def chat_api_with_backoff(model, messages):
    return openai.ChatCompletion.create(model=model, messages=messages)


def chatgpt_chat_completion(model_id, role, message_content) -> List[str]:
    # Chat completion API call
    completion = chat_api_with_backoff(
        model=model_id,
        messages=[{"role": role, "content": message_content}],
    )
    result = completion.choices[0].message.content
    return [res for res in result.split("\n")]


def create_message(input_list, message_content=MESSAGE_CONTENT) -> str:
    # Input text
    input_words: str = ""
    for i in input_list:
        input_words += f"{i}\n"

    message_content += f"\n{input_words}"
    return message_content


def get_results_from_chatgpt(
    input_list,
    chatgpt_input_output_queue,
    message_content=MESSAGE_CONTENT,
) -> Tuple[List[str], List[str]]:
    message_content = create_message(input_list, message_content)
    result_list: List[str] = chatgpt_chat_completion(MODEL_ID, ROLE, message_content)

    mismatched: List[str] = []
    retry_attempt = 0
    len_input_list, len_result_list = (len(input_list), len(result_list))
    while retry_attempt <= MAX_RETRY_ATTEMPTS and len_input_list != len_result_list:
        print(
            f"Retry attempt #{retry_attempt}: Due to mismatch between I/P & O/P: {len_input_list} & {len_result_list} respectively"
        )
        result_list = chatgpt_chat_completion(MODEL_ID, ROLE, message_content)
        # Update length with the newly computed result list
        len_result_list = len(result_list)
        retry_attempt += 1

    # Store results in a Queue
    if len_input_list == len_result_list:
        chatgpt_input_output_queue.put([input_list, result_list])
        chatgpt_input_output_queue.put(None)
    else:
        # Empty list added to keep write_to_text() function intact
        chatgpt_input_output_queue.put([])
        chatgpt_input_output_queue.put(None)
        mismatched = input_list

    return result_list, mismatched


def write_to_text(chatgpt_queue: Queue, output_file: str, len_input: int):
    written: int = 0

    with open(output_file, "w+", encoding="UTF-8") as fp:
        while True:
            input_output_list = chatgpt_queue.get()

            if input_output_list is None:
                written += 1
                print(f"written value: {written}")
                if written == len_input:
                    break
            else:
                fp.write(f"{input_output_list}\n")
                fp.flush()  # Clear internal buffer of file to continuously monitor


def get_valid_words(input_file=INPUT_FILE) -> List[str]:
    total = 0
    valid_words = set()  # To ensure list is unique
    with open(input_file, "r") as fp:
        if input_file.endswith(".json"):
            raw_data = json.load(fp)
        elif input_file.endswith(".txt"):
            raw_data = fp.readlines()

        word: str
        for word in raw_data:
            word = word.strip()
            word = re.sub("&", " and ", word)
            word = re.sub("\s\s+", " ", word)
            if word:
                clean_word, valid = clean_and_verify_transcript(
                    word, retain_numbers=True
                )
                if valid:
                    valid_words.add(clean_word)
            total += 1

    valid_words = list(sorted(valid_words))
    print(f"Total count of word in raw file: {total}")
    print(f"Length of final count after filtering: {len(valid_words)}")
    print(f"Difference after filtering: {total - len(valid_words)}\n")

    return valid_words


def create_valid_inputs_list(
    valid_words: List[str],
    message_content=MESSAGE_CONTENT,
):
    chatgpt_input_list = []
    tmp_list = []
    is_written = False
    len_message_content = num_tokens_from_string(message_content)
    tokens_length = len_message_content

    for valid_word in valid_words:
        if (
            tokens_length <= INPUT_TOKEN_LENGTH_THRESHOLD
        ):  # 1 token 4 chars in english => 4,097 * 4 = 16,388
            # The length limit applies to the input+output tokens
            # Having half for I/P and half for O/P should work
            # 16,388 / 2 = 8194 ~ 8000
            tmp_list.append(valid_word)
            tokens_length += num_tokens_from_string(valid_word)
            is_written = False
        else:
            chatgpt_input_list.append(tmp_list)
            is_written = True
            tmp_list = []
            tmp_list.append(valid_word)
            tokens_length = len_message_content + num_tokens_from_string(valid_word)
    if is_written is False:  #  when `tmp_list` not in `chatgpt_input_list`
        chatgpt_input_list.append(tmp_list)

    sum_of_length_of_lists_in_input: int = 0
    for ip_list in chatgpt_input_list:
        sum_of_length_of_lists_in_input += len(ip_list)
    average_length_of_lists_in_input: int = int(
        sum_of_length_of_lists_in_input / len(chatgpt_input_list)
    )
    print(f"Average length of lists in input: {average_length_of_lists_in_input}")
    return chatgpt_input_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", help="Path to text or json file with the words", required=True)
    parser.add_argument("--input_audio_format", help="Input audio codec", required=True)
    parser.add_argument(
        "--output_path", help="Path to output concatenated audio files", required=True
    )
    parser.add_argument(
        "--max_audio_length",
        help="Maximum audio length after concatenating in minutes",
        required=True,
    )
    parser.add_argument(
        "--output_prefix",
        help="Name of the prefix in concatenated files",
        required=False,
        default="concatenated_audio",
    )
    args = parser.parse_args()
    
    # Original
    # ^^^^^^^^
    INPUT_FILE = "/home/local/ZOHOCORP/gayathri-12052/workspace/chatgpt/data/locations.txt"
    OUTPUT_FILE = "/home/local/ZOHOCORP/gayathri-12052/workspace/chatgpt/output/locations_chatgpt_output.txt"
    MISMATCH_FILE = "/home/local/ZOHOCORP/gayathri-12052/workspace/chatgpt/output/locations_chatgpt_mismatch.txt"

    locations_message = "Capitalize the below list of locations properly"
    # merchants_message = "Capitalize the below list of names of popular brands properly"
    MESSAGE_CONTENT = locations_message

    # Have a lesser threshold for input as outputs are seeming to get cut and having a mismatch
    # 4096 tokens limit (Input + Output)
    # I/P can be around 2048, but better to be lesser than this
    MAX_RETRY_ATTEMPTS = 6
    INPUT_TOKEN_LENGTH_THRESHOLD = 1000  # Previously, it was 1500
    WORKERS = 16

    # Get the inputs for ChatGPT
    valid_words = get_valid_words(input_file=INPUT_FILE)
    chatgpt_input_list = create_valid_inputs_list(
        valid_words=valid_words,
        message_content=MESSAGE_CONTENT,
    )
    print(f"Length of inputs to ChatGPT: {len(chatgpt_input_list)}\n")

    manager = Manager()
    chatgpt_input_output_queue = manager.Queue()
    chatput_mismatch_queue = manager.Queue()

    ### With Queue
    len_input = len(chatgpt_input_list)
    write_to_text_process = Process(
        target=write_to_text, args=(chatgpt_input_output_queue, OUTPUT_FILE, len_input)
    )
    write_to_text_process.start()
    start = time.time()
    parallel = Parallel(n_jobs=WORKERS, prefer="processes", backend="multiprocessing")
    results_and_mismatched = parallel(
        [
            delayed(get_results_from_chatgpt)(
                chatgpt_input, chatgpt_input_output_queue, MESSAGE_CONTENT
            )
            for chatgpt_input in tqdm(chatgpt_input_list)
        ]
    )
    end = time.time()
    write_to_text_process.join()
    print(f"Time taken: {end-start}s")

    with open(MISMATCH_FILE, "w") as fp:
        for results_mismatched in results_and_mismatched:
            _, mismatched = results_mismatched
            if mismatched:
                fp.write(f"{mismatched}\n")
