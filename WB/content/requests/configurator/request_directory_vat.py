from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.configurator.response_directory_vat import (
    ResponseDirectoryVat,
)

from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/directory/vat"


class RequestDirectoryVatAPI(AbsRequestExecutor):
    """
    **Ставка НДС**

    'С помощью данного метода можно получить список значений для характеристики
     **Ставка НДС**.
    """

    def execute(self, locale: str) -> ResponseDirectoryVat:
        """
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """

        url = f"{URL}?{locale=}" if locale else URL
        response = self._get(url)
        if response:
            return from_dict(ResponseDirectoryVat, response)
