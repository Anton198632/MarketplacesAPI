from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Photo:
    big: Optional[str] = field(
        default=None, metadata={"description": "URL фото `900х1200`"}
    )
    c246x328: Optional[str] = field(
        default=None, metadata={"description": "URL фото `248х328`"}
    )
    c516x688: Optional[str] = field(
        default=None, metadata={"description": "URL фото `516х688`"}
    )
    square: Optional[str] = field(
        default=None, metadata={"description": "URL фото `600х600`"}
    )
    tm: Optional[str] = field(
        default=None, metadata={"description": "URL фото `75х100`"}
    )
