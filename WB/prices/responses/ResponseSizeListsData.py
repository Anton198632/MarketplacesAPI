from WB.prices.schemas import SizeGood
from dataclasses import dataclass
from typing import List


@dataclass
class ResponseSizeListsData:
    listGoods: SizeGood
