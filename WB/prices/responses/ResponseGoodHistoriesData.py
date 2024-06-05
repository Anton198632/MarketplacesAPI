from WB.prices.schemas import GoodHistory
from dataclasses import dataclass
from typing import List


@dataclass
class ResponseGoodHistoriesData:
    uploadID: int
    historyGoods: GoodHistory
