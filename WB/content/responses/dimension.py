from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Dimension:
    length: Optional[int] = field(
        default=None, metadata={"description": "Длина, см"}
    )
    width: Optional[int] = field(
        default=None, metadata={"description": "Ширина, см"}
    )
    height: Optional[int] = field(
        default=None, metadata={"description": "Высота, см"}
    )

