from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2BarcodesResponse200:
    """
    Генерация баркодов

    Метод позволяет сгенерировать массив уникальных баркодов для создания размера НМ в КТ.
    """
    #  Массив сгенерированных баркодов
    data: List[str]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
