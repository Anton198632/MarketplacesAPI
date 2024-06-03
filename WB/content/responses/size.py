from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Size:
    chrtID: Optional[int] = field(
        default=None,
        metadata={
            "description": (
                "Числовой идентификатор размера для данного артикула WB"
            ),
        },
    )
    techSize: Optional[str] = field(
        default=None,
        metadata={"description": "Размер товара (А, XXL, 57 и др.)"},
    )
    wbSize: Optional[str] = field(
        default=None, metadata={"description": "Российский размер товара"}
    )
    skus: List[str] = field(
        default_factory=list, metadata={"description": "Баркод товара"}
    )

