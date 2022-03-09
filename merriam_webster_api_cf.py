import time
import concurrent.futures
import requests
import random

NUM_WORDS = 300

BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # <1>

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # <2>
PARAMS = {'key': API_KEY}

WORDS = []

def main():
    load_words()
    serial_time = get_time(get_words_serial)
    print(f"serial function took {serial_time:.1f} seconds\n")
    concurrent_time = get_time(get_words_concurrent)
    print(f"concurrent function took {concurrent_time:.1f} seconds\n")

def get_time(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

def load_words():
    with open('DATA/words.txt') as words_in:
        all_words = words_in.read().splitlines()
        WORDS.extend(random.sample(all_words, NUM_WORDS))

def get_word_info(word, timeout):
    """
    Retrieve contents of one URL.
    """
    url = BASE_URL + word
    with requests.get(url, params=PARAMS, timeout=timeout) as response:
        if response.status_code != requests.codes.OK:
            raise Exception("Unable to reach URL")

        word_info = ""
        data = response.json()  # <4>
        for entry in data: # <5>
            if isinstance(entry, dict):
                short_def = entry.get('shortdef')
                if short_def:
                    word_info += f"{word.upper()} {' '.join(short_def)}\n"
        return word_info

def get_words_serial():
    """
    Retrieve data from URLs one at a time
    """
    print("** SERIAL **")
    for word in WORDS:
        try:
            word_data = get_word_info(word, 60)
        except Exception as exc:
            print(f'{word} generated an exaception: {exc}')
        else:
            print(word_data)

def get_words_concurrent():
    """
    Retrieve data from URLs concurrently
    """
    print("** CONCURRENT **")
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(get_word_info, word, 60): word for word in WORDS}
        for future in concurrent.futures.as_completed(future_to_url):
            word = future_to_url[future]
            try:
                word_info = future.result()
            except Exception as exc:
                print(f'{word} generated an exception: {exc}')
            else:
                print(word_info)


if __name__ == '__main__':
    main()
