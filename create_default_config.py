import json

ORIGINAL = 'data/default_config.txt'

with open(ORIGINAL, 'r') as f:
    lines = f.read().split('\n')

output_json = {}

for line in lines:
    if not line:
        continue
    key, value = line.split(' = ')
    try:
        new_value = int(value)
        output_json[key] = new_value
        continue
    except ValueError:
        pass

    try:
        new_value = float(value)
    except ValueError:
        new_value = value
    output_json[key] = new_value


target = 'data/default_config.json'

with open(target, 'w') as f:
    json.dump(output_json, f, indent=2)


