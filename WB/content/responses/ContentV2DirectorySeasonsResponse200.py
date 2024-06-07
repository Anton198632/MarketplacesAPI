from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2DirectorySeasonsResponse200:
    """
    Сезон

    Получение значения характеристики Сезон.
    """
    #  Массив значений для хар-ки Сезон
    data: List[str]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
