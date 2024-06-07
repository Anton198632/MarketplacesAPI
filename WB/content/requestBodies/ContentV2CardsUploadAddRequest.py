from typing import List
from WB.content.requestBodies import ContentV2CardsUploadAddRequestCardsToAdd
from dataclasses import dataclass


@dataclass
class ContentV2CardsUploadAddRequest:
    """
    Добавление НМ к КТ
    Метод позволяет добавить к карточке товара новую номенклатуру. <span class=
    "newM">new</span> <br> 
    Добавление НМ к КТ происходит асинхронно, после отправки запрос станови
    тся в очередь на обработку.<br> 
    `Важно!` Если после успешной отправки запроса номенклатура не создалась
    , то необходимо проверить раздел "Список несозданных НМ с ошибками". <br> 
    Для того чтобы убрать НМ из ошибочных, необходимо повторно сделать запр
    ос с исправленными ошибками.<br>
    Максимальный размер запроса 10 Мб.
        Габариты товаров можно указать только в **сантиметрах**.
    """
    #  imtID КТ, к которой добавляется НМ
    imtID: int
    #  Структура добавляемой НМ
    cardsToAdd: List[ContentV2CardsUploadAddRequestCardsToAdd]
