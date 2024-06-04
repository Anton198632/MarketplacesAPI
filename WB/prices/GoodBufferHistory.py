from dataclasses import dataclass
from typing import Optional


@dataclass
class GoodBufferHistory:
    nmID: Optional[int]
    vendorCode: Optional[str]
    sizeID: Optional[int]
    techSizeName: Optional[str]
    price: Optional[int]
    currencyIsoCode4217: Optional[str]
    discount: Optional[int]
    status: None
    errorText: Optional[str]
