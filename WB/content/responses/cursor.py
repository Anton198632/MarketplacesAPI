from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Cursor:
    nmID: Optional[int] = field(
        default=None,
        metadata={
            "description": (
                "Номер Артикула WB с которой надо запрашивать следующий"
                " список КТ"
            )
        }
    )
    total: Optional[int] = field(
        default=None, metadata={"description": "Кол-во возвращенных КТ"}
    )
