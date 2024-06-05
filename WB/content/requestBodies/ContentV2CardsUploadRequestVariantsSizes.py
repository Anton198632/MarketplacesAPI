from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2CardsUploadRequestVariantsSizes:
    techSize: str
    wbSize: str
    price: int
    skus: List[str]
