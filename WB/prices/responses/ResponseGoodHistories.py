from WB.prices.responses import ResponseGoodHistoriesData
from dataclasses import dataclass


@dataclass
class ResponseGoodHistories:
    """
    Информация о товарах в загрузке
    """

    data: ResponseGoodHistoriesData
