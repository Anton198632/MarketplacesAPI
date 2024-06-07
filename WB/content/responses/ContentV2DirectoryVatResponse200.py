from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2DirectoryVatResponse200:
    """
    Ставка НДС
    С помощью данного метода можно получить список значений для характеристики 
    **Ставка НДС**. <span class="newM">new</span>
    """

    data: List[str]
    #  Флаг наличия ошибки
    error: bool
    #  Текст ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
