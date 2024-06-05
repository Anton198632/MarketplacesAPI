from WB.prices.schemas import GoodBufferHistory
from dataclasses import dataclass
from typing import List


@dataclass
class ResponseGoodBufferHistoriesData:
    uploadID: int
    bufferGoods: GoodBufferHistory
