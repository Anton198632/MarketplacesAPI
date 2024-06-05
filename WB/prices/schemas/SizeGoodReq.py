from dataclasses import dataclass


@dataclass
class SizeGoodReq:
    nmID: int
    sizeID: int
    price: int
