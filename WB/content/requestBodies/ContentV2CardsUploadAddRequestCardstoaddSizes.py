from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2CardsUploadAddRequestCardstoaddSizes:
    techSize: str
    wbSize: str
    price: int
    skus: List[str]
