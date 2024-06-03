from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Tag:
    id: Optional[int] = field(
        default=None, metadata={"description": "Идентификатор тега"}
    )
    name: Optional[str] = field(
        default=None, metadata={"description": "Название тега"}
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "description": (
                "Цвет тега. Доступные цвета: D1CFD7 - серый, FEE0E0 - красный,"
                " ECDAFF - фиолетовый, E4EAFF - синий, DEF1DD - зеленый,"
                " FFECC7 - желтый"
            )
        }
    )
