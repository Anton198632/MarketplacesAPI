from WB.prices.schemas import GoodsList
from dataclasses import dataclass
from typing import List


@dataclass
class ResponseGoodsListsData:
    listGoods: GoodsList
