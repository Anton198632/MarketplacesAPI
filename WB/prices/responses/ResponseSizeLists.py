from WB.prices.responses import ResponseSizeListsData
from dataclasses import dataclass


@dataclass
class ResponseSizeLists:
    """
    Размеры
    """

    data: ResponseSizeListsData
    #  Флаг ошибки
    error: bool
    #  Текст ошибки
    errorText: str
