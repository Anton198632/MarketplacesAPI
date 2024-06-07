from WB.prices.schemas import GoodsList
from typing import List
from dataclasses import dataclass


@dataclass
class ResponseGoodsListsData:

    listGoods: GoodsList
