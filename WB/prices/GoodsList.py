import List
from dataclasses import dataclass
from typing import Optional
from typing import List


@dataclass
class GoodsList:
    nmID: Optional[int]
    vendorCode: Optional[str]
    sizes: list[GoodsList_sizes]
    currencyIsoCode4217: Optional[str]
    discount: Optional[int]
    editableSizePrice: bool
