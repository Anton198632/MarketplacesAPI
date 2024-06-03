from dataclasses import dataclass, field
from typing import List

from WB.content.requests.card import Card


@dataclass
class UploadAddData:
    imtID: int = field(
        metadata={"description": "imtID КТ, к которой добавляется НМ"}
    )
    cardsToAdd: List[Card] = field(
        default_factory=list,
        metadata={"description": "Структура добавляемой НМ"},
    )
