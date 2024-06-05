from dataclasses import dataclass


@dataclass
class GoodsListSizes:
    sizeID: int
    price: int
    discountedPrice: int
    techSizeName: str
