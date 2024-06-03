from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Characteristic:
    id: Optional[int] = field(
        default=None, metadata={"description": "ID характеристики"}
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "description": (
                "Значение характеристики. Тип значения зависит от"
                " типа характеристики"
            ),
        }
    )
