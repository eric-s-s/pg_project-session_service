import json
import os

from session_service import DATA_DIR


def get_defaults_json():
    return {
        'config': get_default_config(),
        'word_lists': get_default_word_lists()
    }


def get_default_config():
    default_config = 'default_config.json'
    return _get_json_from_data_dir(default_config)


def get_default_word_lists():
    default_word_lists = 'default_word_lists.json'
    return _get_json_from_data_dir(default_word_lists )


def _get_json_from_data_dir(default_config):
    with open(os.path.join(DATA_DIR, default_config), 'r') as f:
        answer = json.load(f)
    return answer