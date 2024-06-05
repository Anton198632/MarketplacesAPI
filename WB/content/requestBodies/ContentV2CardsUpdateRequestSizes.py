from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2CardsUpdateRequestSizes:
    chrtID: int
    techSize: str
    wbSize: str
    skus: List[str]
