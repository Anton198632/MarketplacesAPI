from typing import List
from dataclasses import dataclass, field

from WB.content.requests.viewing.cards_list_data import Settings


@dataclass
class CardsDeleteTrashData:
    nmIDs: List[int] = field(
        metadata={"description": "Артикул WB (max. 1000)"}
    )


@dataclass
class CardsRecoveryData:
    nmIDs: List[int] = field(
        metadata={"description": "Артикул WB (max. 1000)"}
    )


@dataclass
class CardsTrashData:
    settings: Settings = field(
        default=Settings, metadata={"description": "Настройки"}
    )
