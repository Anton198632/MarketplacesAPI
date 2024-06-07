from WB.prices.responses import ResponseGoodBufferHistoriesData
from dataclasses import dataclass


@dataclass
class ResponseGoodBufferHistories:
    """
    Информация о товарах в загрузке
    """

    data: ResponseGoodBufferHistoriesData
    #  Флаг ошибки
    error: bool
    #  Текст ошибки
    errorText: str
