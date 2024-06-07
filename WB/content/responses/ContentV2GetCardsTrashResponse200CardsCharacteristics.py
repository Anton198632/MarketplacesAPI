from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsTrashResponse200CardsCharacteristics:

    id: int

    name: str

    value: List[str]
