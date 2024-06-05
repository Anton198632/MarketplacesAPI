from dataclasses import dataclass


@dataclass
class SizeGood:
    nmID: int
    sizeID: int
    vendorCode: str
    price: int
    currencyIsoCode4217: str
    discountedPrice: int
    discount: int
    techSizeName: str
    editableSizePrice: bool
