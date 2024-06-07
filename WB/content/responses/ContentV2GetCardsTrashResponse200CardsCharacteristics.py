from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2GetCardsTrashResponse200CardsCharacteristics:

    id: int

    name: str

    value: List[str]
