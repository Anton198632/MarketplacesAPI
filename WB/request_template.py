import requests
from WB.create_logger import create_logger

logger = create_logger(__name__)

SERVER = "https://suppliers-api.wildberries.ru"


class APINAMEClass:
    """
    DESCRIPTION
    """
    def __init__(self, api_key):
        self.__headers = {"Authorization": f"{api_key}"}

    def METHOD(self, url, body):
        response = requests.post(url=url)

