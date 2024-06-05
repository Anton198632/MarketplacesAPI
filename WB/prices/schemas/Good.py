from dataclasses import dataclass


@dataclass
class Good:
    nmID: int
    price: int
    discount: int
