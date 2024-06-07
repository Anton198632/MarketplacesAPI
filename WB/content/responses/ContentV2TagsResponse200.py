from types import NoneType
from dataclasses import dataclass


@dataclass
class ContentV2TagsResponse200:
    """
    Список тегов
    Метод позволяет получить список существующих тегов продавца.
    """

    data: NoneType
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
