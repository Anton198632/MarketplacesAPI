import json

import requests

if __name__ == '__main__':
    response = requests.get("https://openapi.wildberries.ru/content/api/ru/")
    text = response.text

    redoc_state = text[text.find("__redoc_state = ") + 16 :]
    redoc_state = redoc_state[0 : redoc_state.find(";\n")]

    api_json = json.loads(redoc_state)

    pass
