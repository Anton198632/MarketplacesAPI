from WB.prices.responses import ResponseGoodHistoriesData
from dataclasses import dataclass


@dataclass
class ResponseGoodHistories:
    data: ResponseGoodHistoriesData
