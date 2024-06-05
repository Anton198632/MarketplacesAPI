from WB.prices.schemas import GoodStatus
from dataclasses import dataclass


@dataclass
class GoodHistory:
    nmID: int
    vendorCode: str
    sizeID: int
    techSizeName: str
    price: int
    currencyIsoCode4217: str
    discount: int
    status: GoodStatus
    errorText: str
