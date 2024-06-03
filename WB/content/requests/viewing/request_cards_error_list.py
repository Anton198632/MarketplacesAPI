from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.viewing.response_cards_error_list import (
    ResponseCardsErrorList
)
from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/cards/error/list"


class RequestCardsErrorListAPI(AbsRequestExecutor):
    """
    **Список несозданных номенклатур (НМ) с ошибками**

    Метод позволяет получить список НМ и список ошибок которые произошли во
     время создания КТ. <br>`ВАЖНО`: Для того чтобы убрать НМ из ошибочных,
      надо повторно сделать запрос с исправленными ошибками на создание КТ.
    """

    def execute(self, locale: Optional[str]) -> ResponseCardsErrorList:
        """
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """

        url = f"{URL}?{locale=}" if locale else URL
        response = self._get(url)
        if response:
            return from_dict(ResponseCardsErrorList, response)
