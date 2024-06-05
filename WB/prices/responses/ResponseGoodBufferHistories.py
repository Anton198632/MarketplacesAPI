from WB.prices.responses import ResponseGoodBufferHistoriesData
from dataclasses import dataclass


@dataclass
class ResponseGoodBufferHistories:
    data: ResponseGoodBufferHistoriesData
    error: bool
    errorText: str
