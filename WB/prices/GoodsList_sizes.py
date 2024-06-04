from dataclasses import dataclass
from typing import Optional


@dataclass
class GoodsList_sizes:
    sizeID: Optional[int]
    price: Optional[int]
    discountedPrice: None
    techSizeName: Optional[str]
