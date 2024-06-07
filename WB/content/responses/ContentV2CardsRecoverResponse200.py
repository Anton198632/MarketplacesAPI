from typing import Any
from typing import Dict
from typing import Optional
from dataclasses import dataclass


@dataclass
class ContentV2CardsRecoverResponse200:
    """
    Восстановление НМ из корзины

    Метод позволяет восстановить НМ из корзины. <span class="newM">new</span><br> <code>ВАЖНО</code>: При восстановлении НМ из корзины она не возвращается в КТ в которой была до переноса в корзину, то есть <code>imtID</code> остается тот же, что и был у НМ в корзине.
    
    """

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: Optional[Dict]
