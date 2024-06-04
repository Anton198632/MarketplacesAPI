from dataclasses import dataclass
from typing import Optional


@dataclass
class SizeGoodReq:
    nmID: Optional[int]
    sizeID: Optional[int]
    price: Optional[int]
