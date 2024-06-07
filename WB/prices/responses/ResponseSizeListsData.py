from WB.prices.schemas import SizeGood
from typing import List
from dataclasses import dataclass


@dataclass
class ResponseSizeListsData:

    listGoods: SizeGood
