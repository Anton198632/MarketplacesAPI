from WB.prices.schemas import GoodStatusBuffer
from dataclasses import dataclass


@dataclass
class GoodBufferHistory:
    nmID: int
    vendorCode: str
    sizeID: int
    techSizeName: str
    price: int
    currencyIsoCode4217: str
    discount: int
    status: GoodStatusBuffer
    errorText: str
