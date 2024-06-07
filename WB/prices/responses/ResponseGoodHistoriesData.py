from typing import List
from WB.prices.schemas import GoodHistory
from dataclasses import dataclass


@dataclass
class ResponseGoodHistoriesData:
    #  ID загрузки
    uploadID: int

    historyGoods: GoodHistory
