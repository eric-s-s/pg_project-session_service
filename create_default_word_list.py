VERBS = 'data/verbs.csv'
COUNTABLE_NOUNS = 'data/nouns.csv'
UNCOUNTABLE_NOUNS = 'data/uncountable.csv'

from csv import DictReader
import json

file_names = (VERBS, COUNTABLE_NOUNS, UNCOUNTABLE_NOUNS)
keys = ('verb_groups', 'countable_nouns', 'uncountable_nouns')

output_json = {'static_nouns': []}


def int_the_objects(element):
    element['objects'] = int(element['objects'])
    return element


for f_name, json_key in zip(file_names, keys):
    with open(f_name) as f:
        reader = DictReader(f)
        new_json = list(reader)
        if json_key == 'verb_groups':
            new_json = [int_the_objects(el) for el in new_json]
        output_json[json_key] = new_json

target = 'data/default_word_lists.json'
with open(target, 'w') as f:
    json.dump(output_json, f, indent=2)
