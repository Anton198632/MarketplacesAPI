from WB.content.responses import ContentV2GetCardsListResponse200Cards
from WB.content.responses import ContentV2GetCardsListResponse200Cursor
from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListResponse200:
    """
    Список номенклатур (НМ)
    Метод позволяет получить список созданных НМ с фильтрацией по разным параме
    трам, пагинацией и сортировкой. 
    <br> *Важно*. Карточки, находящиеся в корзине, в ответе метода не выдаю
    тся. <br> Получить такие карточки можно только методом "Список НМ, находящи
    хся в корзине".<br> <br>Порядок работы с `get/cards/list`: <br> Чтобы получ
    ить полный список номенклатур, <b>если их больше 100</b>, необходимо воспол
    ьзоваться пагинацией.
      <ol>
        <li>Сделать первый запрос (все указанные ниже параметры обязательны
    ): <br>
          <pre style="background-color: rgb(38 50 56 / 5%); color: #e53935"
    >
        {
          "settings": {                      "cursor": {
              "limit": 100
            },
            "filter": {
              "withPhoto": -1
            }
          }
        }</pre>                       </li>
        <li>Пройти в конец полученного списка номенклатур, скопировать из <
    code>cursor</code> две строки:
          <ul>
        <li><code>"updatedAt": "***"</code>,</li>
        <li><code>"nmID": ***</code>,</li>
          </ul>
        <li>Вставить скопированные строки в <code>cursor</code> запроса, по
    вторить вызов метода. </li>
        <li>Повторять пункты <b>2</b> и <b>3</b>, пока <code>total</code> в
     ответе не станет меньше чем <code>limit</code> в запросе.
          <br>Это будет означать, что Вы получили все карточки.
      </ol>
      <br> По желанию можно добавить поиск и сортировку. См описание в <b>R
    equest Body schema</b>
      <br> В <b>Request samples</b> представлен пример запроса со всеми воз
    можными параметрами. 
    """
    #  Список КТ
    cards: List[ContentV2GetCardsListResponse200Cards]
    #  Пагинатор
    cursor: ContentV2GetCardsListResponse200Cursor
