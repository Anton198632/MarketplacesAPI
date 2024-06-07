from dataclasses import dataclass
from WB.prices.responses import ResponseSizeListsData


@dataclass
class ResponseSizeLists:
    """
    Размеры

    
    """

    Data: ResponseSizeListsData
    #  Флаг ошибки
    error: bool
    #  Текст ошибки
    errorText: str
