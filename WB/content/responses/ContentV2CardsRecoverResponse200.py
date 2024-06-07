from typing import Optional
from typing import Dict
from typing import Any
from dataclasses import dataclass


@dataclass
class ContentV2CardsRecoverResponse200:
    """
    Восстановление НМ из корзины
    Метод позволяет восстановить НМ из корзины. <span class="newM">new</span><b
    r> <code>ВАЖНО</code>: При восстановлении НМ из корзины она не возвращается
     в КТ в которой была до переноса в корзину, то есть <code>imtID</code> оста
    ется тот же, что и был у НМ в корзине.
    """

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: Optional[Dict]
