from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.configurator.response_directory_tnved import (
    ResponseDirectoryTnved,
)

from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/directory/tnved"


class RequestDirectoryTnvedAPI(AbsRequestExecutor):
    """
    **ТНВЭД код**

    С помощью данного метода можно получить список ТНВЭД кодов по ID предмета
     и фильтру по ТНВЭД коду.
    """

    def execute(
        self, subjectId: int, search: Optional[int],  locale: Optional[str]
    ) -> ResponseDirectoryTnved:
        """
        :param search: Поиск по ТНВЭД-коду. Работает только в паре с subjectID
        :param subjectId: Идентификатор предмета
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """

        url = f"{URL}?{locale=}" if locale else URL
        response = self._get(url)
        if response:
            return from_dict(ResponseDirectoryTnved, response)
