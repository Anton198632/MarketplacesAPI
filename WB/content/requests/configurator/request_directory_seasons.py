from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.configurator.response_directory_seasons import (
    ResponseDirectorySeasons,
)

from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/directory/seasons"


class RequestDirectorySeasonsAPI(AbsRequestExecutor):
    """
    **Сезон**

    Получение значения характеристики Сезон.
    """

    def execute(self, locale: Optional[str]) -> ResponseDirectorySeasons:
        """
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """

        url = f"{URL}?{locale=}" if locale else URL
        response = self._get(url)
        if response:
            return from_dict(ResponseDirectorySeasons, response)
