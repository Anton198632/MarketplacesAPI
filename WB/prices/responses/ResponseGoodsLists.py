from WB.prices.responses import ResponseGoodsListsData
from dataclasses import dataclass


@dataclass
class ResponseGoodsLists:
    data: ResponseGoodsListsData
