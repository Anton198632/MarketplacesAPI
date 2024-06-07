from WB.content.requestBodies import ContentV2GetCardsTrashRequestSettings
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsTrashRequest:
    """
    Список НМ, находящихся в корзине
    Метод позволяет получить список НМ, находящихся в корзине.  <br> <br>Порядо
    к работы. <br> Чтобы получить полный список номенклатур, <b>если их больше 
    100</b>, необходимо воспользоваться пагинацией.
      <ol>
        <li>Сделать первый запрос (все указанные ниже параметры обязательны
    ): <br>
          <pre style="background-color: rgb(38 50 56 / 5%); color: #e53935"
    >
        {
          "settings": {                      "cursor": {
              "limit": 100
            }
          }
        }</pre>                       </li>
        <li>Пройти в конец полученного списка номенклатур, скопировать из <
    code>cursor</code> две строки:
          <ul>
        <li><code>"trashedAt": "***"</code>,</li>
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
    #  Настройки
    settings: ContentV2GetCardsTrashRequestSettings
