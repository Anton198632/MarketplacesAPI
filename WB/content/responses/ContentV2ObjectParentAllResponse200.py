from types import NoneType
from dataclasses import dataclass


@dataclass
class ContentV2ObjectParentAllResponse200:
    """
    Родительские категории товаров
    С помощью данного метода можно получить список всех родительских категорий 
    товаров.
    """

    data: NoneType
    #  Флаг наличия ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
