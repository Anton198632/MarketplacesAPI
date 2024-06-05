from WB.prices.schemas import GoodsListSizes
from dataclasses import dataclass
from typing import List


@dataclass
class GoodsList:
    nmID: int
    vendorCode: str
    sizes: List[GoodsListSizes]
    currencyIsoCode4217: str
    discount: int
    editableSizePrice: bool
