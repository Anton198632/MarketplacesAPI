import abc
from typing import Any, Optional

import requests

from WB.create_logger import create_logger

logger = create_logger(__name__)

SERVER = "https://suppliers-api.wildberries.ru"


class AbsRequestExecutor:
    _RESPONSE_OK_200 = 200
    _RESPONSE_OK_201 = 201
    _RESPONSE_OK_204 = 204

    def __init__(self, api_key):
        self.__headers = {"Authorization": f"{api_key}"}

    def _add_header(self, key, value):
        self.__headers[key] = value

    def _get(self, url):
        response = requests.get(url=url, headers=self.__headers)

        if (
            response.status_code == self._RESPONSE_OK_200
            or response.status_code == self._RESPONSE_OK_201
        ):
            logger.info(response.status_code)
            content_type = response.headers.get("Content-Type")
            if "application/pdf" in content_type:
                return {"pdf_content": response.content}
            elif "application/json" in content_type:
                return response.json()
            else:
                return None
        else:
            logger.warning(f"{response.status_code} {response.json()}")

    def _post(
        self,
        url,
        json: Optional[dict] = None,
        data: Optional[bytes] = None,
        content_type: str = "application/json"
    ):
        response = requests.post(
            url=url,
            headers={**self.__headers, "Content-Type": content_type},
            json=json,
            data=data
        )

        if (
            response.status_code == self._RESPONSE_OK_200
            or response.status_code == self._RESPONSE_OK_201
        ):
            logger.info(response.status_code)
            content_type = response.headers.get("Content-Type")
            if "application/pdf" in content_type:
                return {"pdf_content": response.content}
            elif "application/json" in content_type:
                return response.json()
            else:
                return None
        else:
            logger.warning(f"{response.status_code} {response.json()}")

    def _patch(self, url, json=None):
        response = requests.patch(
            url,
            headers={**self.__headers, "Content-Type": "application/json"},
            json=json,
        )
        if response.status_code == self._RESPONSE_OK_204:
            return True
        else:
            logger.warning(f"{response.status_code} {response.text}")

    def _delete(self, url, json=None):
        response = requests.delete(
            url,
            headers={**self.__headers, "Content-Type": "application/json"},
            json=json,
        )
        if response.status_code == self._RESPONSE_OK_204:
            return True
        else:
            logger.warning(f"{response.status_code} {response.text}")

    @abc.abstractmethod
    def execute(self, *args) -> Any:
        pass
