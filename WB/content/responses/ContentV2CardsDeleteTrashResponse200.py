from typing import Any
from typing import Dict
from typing import Optional
from dataclasses import dataclass


@dataclass
class ContentV2CardsDeleteTrashResponse200:
    """
    Перенос НМ в корзину

    Метод позволяет перенести НМ в корзину. Перенос карточки в корзину не является удалением карточки. <span class="newM">new</span><br> <code>ВАЖНО</code>: При переносе НМ в корзину, данная НМ выходит из КТ, то есть ей присваивается новый <code>imtID</code>.<br> Карточка товара удаляется автоматически, если лежит в корзине больше 30 дней.<br> Корзина зачищается от карточек, лежащих в ней более 30 дней, каждую ночь по Московскому времени.
    
    """

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: Optional[Dict]
