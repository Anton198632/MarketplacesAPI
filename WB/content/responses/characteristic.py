from dataclasses import dataclass, field
from typing import Optional, Any


@dataclass
class Characteristic:
    id: Optional[int] = field(
        default=None, metadata={"description": "Идентификатор характеристики"})
    name: Optional[str] = field(
        default=None, metadata={"description": "Название характеристики"})
    value: Optional[Any] = field(
        default=None,
        metadata={
            "description": (
                "Значение характеристики. Тип значения зависит от типа"
                " характеристики"
            )
        }
    )
