from WB.prices.schemas import GoodBufferHistory
from typing import List
from dataclasses import dataclass


@dataclass
class ResponseGoodBufferHistoriesData:
    #  ID загрузки
    uploadID: int

    bufferGoods: GoodBufferHistory
