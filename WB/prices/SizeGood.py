from dataclasses import dataclass
from typing import Optional


@dataclass
class SizeGood:
    nmID: Optional[int]
    sizeID: Optional[int]
    vendorCode: Optional[str]
    price: Optional[int]
    currencyIsoCode4217: Optional[str]
    discountedPrice: None
    discount: Optional[int]
    techSizeName: Optional[str]
    editableSizePrice: bool
