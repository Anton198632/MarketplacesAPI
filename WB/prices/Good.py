from dataclasses import dataclass
from typing import Optional


@dataclass
class Good:
    nmID: Optional[int]
    price: Optional[int]
    discount: Optional[int]
