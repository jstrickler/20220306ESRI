#!/usr/bin/env python
from multiprocessing.dummy import Pool  # <1>
from pprint import pprint
import requests

POOL_SIZE = 4

BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # <2>

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # <3>

search_terms = [  # <4>
    'wombat',
    'frog', 'muntin', 'automobile', 'green', 'connect',
    'vial', 'battery', 'computer', 'sing', 'park',
    'ladle', 'ram', 'dog', 'scalpel'
]


def fetch_data(term):  # <5>
    try:
        response = requests.get(
            BASE_URL + term,
            params={'key': API_KEY},
        )  # <6>
    except requests.HTTPError as err:
        print(err)
        return []
    else:
        data = response.json()  # <7>
        parts_of_speech = []
        for entry in data: # <8>
            if isinstance(entry, dict):
                meta = entry.get("meta")
                if meta:
                    part_of_speech = entry.get("fl")
                    if part_of_speech:
                        parts_of_speech.append(part_of_speech)
        return sorted(set(parts_of_speech))  # <9>


p = Pool(POOL_SIZE)  # <10>

results = p.map(fetch_data, search_terms)  # <11>

for search_term, result in zip(search_terms, results):  # <12>
    print("{}:".format(search_term.upper()))
    if result:
        print(result)
    else:
        print("** no results **")
