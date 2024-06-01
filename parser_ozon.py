import json

import requests

if __name__ == '__main__':
    response = requests.get("https://docs.ozon.ru/api/seller/swagger.json")
    text = response.text
    api_json = json.loads(text)

    pass
