from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.configurator.response_directory_countries import (
    ResponseDirectoryCountries,
)

from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/directory/countries"


class RequestDirectoryCountriesAPI(AbsRequestExecutor):
    """
    **Страна Производства**

    Получение значения характеристики Страна Производства.
    """

    def execute(self, locale: Optional[str]) -> ResponseDirectoryCountries:
        """
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """

        url = f"{URL}?{locale=}" if locale else URL
        response = self._get(url)
        if response:
            return from_dict(ResponseDirectoryCountries, response)
