from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Size:
    techSize: Optional[str] = field(
        default=None, metadata={"description": "Размер товара (XL, 42 и др.)"}
    )
    wbSize: Optional[str] = field(
        default=None, metadata={"description": "Российский размер товара"}
    )
    price: Optional[int] = field(
        default=None, metadata={"description": "Цена товара"}
    )
    skus: Optional[List[str]] = field(
        default_factory=list, metadata={"description": "Баркод"}
    )
