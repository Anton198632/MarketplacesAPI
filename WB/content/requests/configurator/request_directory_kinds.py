from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.configurator.response_directory_kinds import (
    ResponseDirectoryKinds,
)

from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/directory/kinds"


class RequestDirectoryKindsAPI(AbsRequestExecutor):
    """
    **Пол**

    Получение значения характеристики пол.
    """

    def execute(self, locale: Optional[str]) -> ResponseDirectoryKinds:
        """
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """

        url = f"{URL}?{locale=}" if locale else URL
        response = self._get(url)
        if response:
            return from_dict(ResponseDirectoryKinds, response)
