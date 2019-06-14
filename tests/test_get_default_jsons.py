import json
import os
import unittest

from session_service import DATA_DIR
from session_service.get_default_jsons import get_default_config, get_default_word_lists, get_defaults_json


class TestGetDefaultJsons(unittest.TestCase):
    def test_get_default_config(self):
        with open(os.path.join(DATA_DIR, 'default_config.json'), 'r') as f:
            expected_config = json.load(f)
        self.assertEqual(expected_config, get_default_config())

    def test_get_default_word_lists(self):
        with open(os.path.join(DATA_DIR, 'default_word_lists.json'), 'r') as f:
            expected_word_lists = json.load(f)
        self.assertEqual(expected_word_lists, get_default_word_lists())

    def test_get_defaults_json(self):
        expected = {
            'config': get_default_config(),
            'word_lists': get_default_word_lists()
        }
        self.assertEqual(get_defaults_json(), expected)