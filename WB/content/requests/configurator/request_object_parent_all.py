from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER

from WB.content.responses.configurator.response_object_parent_all import (
    ResponseObjectParentAll,
)
from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/object/parent/all"


class RequestObjectParentAllAPI(AbsRequestExecutor):
    """
    **Родительские категории товаров**

    С помощью данного метода можно получить список всех родительских категорий
     товаров.
    """

    def execute(self, locale: Optional[str]) -> ResponseObjectParentAll:
        """
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """

        url = f"{URL}?{locale=}" if locale else URL
        response = self._get(url)
        if response:
            return from_dict(ResponseObjectParentAll, response)
