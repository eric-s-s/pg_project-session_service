import json
import os

import requests
from bind_json_error_handlers import bind_json_error_handlers
from flask import Flask

from session_service import DATA_DIR
from session_service.get_default_jsons import get_defaults_json


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    bind_json_error_handlers(app)

    if test_config is None:
        app.config.from_pyfile('config.py')
        print(app.config)
    else:
        app.config.from_mapping(test_config)


    paragraph_generator_service = app.config.get('PARAGRAPH_GENERATOR_URL')

    print(app.instance_path)

    json_data = get_defaults_json()


    @app.route('/new')
    def get_new():
        target_url = f"{paragraph_generator_service}/generate"
        request = requests.get(target_url, data=json_data)
        # raise requests.exceptions.
        return request.json()

    @app.route('/check')
    def get_check():
        pass

    return app


if __name__ == '__main__':
    create_app().run()
