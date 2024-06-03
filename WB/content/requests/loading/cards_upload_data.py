from dataclasses import dataclass, field
from typing import List

from WB.content.requests.card import Card


@dataclass
class Subject:
    subjectID: int = field(metadata={"description": "ID предмета"})
    variants: List[Card] = field(
        default_factory=list,
        metadata={
            "description": (
                "Массив вариантов товара. В каждой КТ может быть не более 30"
                " вариантов (НМ)"
            )
        }
    )
