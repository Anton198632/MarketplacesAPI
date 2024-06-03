from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.requests.trash.cards_trash_data import CardsTrashData
from WB.content.responses.trash.response_trash import ResponseGetCardsTrash
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/get/cards/trash"


class RequestCardsUpdateAPI(AbsRequestExecutor):
    """
    **Список НМ, находящихся в корзине**

      Метод позволяет получить список НМ, находящихся в корзине.
      <br> <br>Порядок работы. <br> Чтобы получить полный список номенклатур,
       <b>если их больше 100</b>, необходимо воспользоваться пагинацией.
      <ol>
        <li>Сделать первый запрос (все указанные ниже параметры обязательны):
         <br>
          <pre style="background-color: rgb(38 50 56 / 5%); color: #e53935">
            {
              "settings": {
                "cursor": {
                  "limit": 100
                }
              }
            }</pre>
        </li>
        <li>Пройти в конец полученного списка номенклатур, скопировать из
         <code>cursor</code> две строки:
          <ul>
            <li><code>"trashedAt": "***"</code>,</li>
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
        self, locale: Optional[str], card_trash_data: CardsTrashData
    ) -> ResponseGetCardsTrash:
        """
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """
        response = self._post(url=URL, json=to_dict(card_trash_data))
        if response:
            return from_dict(ResponseGetCardsTrash, response)
