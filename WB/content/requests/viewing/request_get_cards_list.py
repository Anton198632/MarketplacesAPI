from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.requests.viewing.cards_list_data import CardsListData
from WB.content.responses.viewing.response_cards_list import ResponseCardList
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/get/cards/list"


class RequestGetCardsListAPI(AbsRequestExecutor):
    """
    **Список номенклатур (НМ)**

    Метод позволяет получить список созданных НМ с фильтрацией по разным
     параметрам, пагинацией и сортировкой.
    <br> *Важно*. Карточки, находящиеся в корзине, в ответе метода не выдаются.
     <br> Получить такие карточки можно только методом "Список НМ, находящихся
      в корзине".<br> <br>Порядок работы с `get/cards/list`: <br> Чтобы
       получить полный список номенклатур, <b>если их больше 100</b>,
        необходимо воспользоваться пагинацией.

      <ol>
        <li>Сделать первый запрос (все указанные ниже параметры обязательны):
         <br>
          <pre style="background-color: rgb(38 50 56 / 5%); color: #e53935">
            {
              "settings": {
                "cursor": {
                  "limit": 100
                },
                "filter": {
                  "withPhoto": -1
                }
              }
            }</pre>
        </li>
        <li>Пройти в конец полученного списка номенклатур, скопировать из
         <code>cursor</code> две строки:
          <ul>
            <li><code>"updatedAt": "***"</code>,</li>
            <li><code>"nmID": ***</code>,</li>
          </ul>
        <li>Вставить скопированные строки в <code>cursor</code> запроса,
         повторить вызов метода. </li>
        <li>Повторять пункты <b>2</b> и <b>3</b>, пока <code>total</code>
         в ответе не станет меньше чем <code>limit</code> в запросе.
          <br>Это будет означать, что Вы получили все карточки.
      </ol>
      <br> По желанию можно добавить поиск и сортировку. См описание в
       <b>Request Body schema</b>
      <br> В <b>Request samples</b> представлен пример запроса со всеми
       возможными параметрами.
    """

    def execute(
            self, locale: Optional[str], card_list_data: CardsListData
    ) -> ResponseCardList:
        """
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """

        url = f"{URL}?{locale=}" if locale else URL
        response = self._post(url=url, json=to_dict(card_list_data))
        if response:
            return from_dict(ResponseCardList, response)
