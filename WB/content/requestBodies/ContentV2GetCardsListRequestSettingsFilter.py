from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2GetCardsListRequestSettingsFilter:
    withPhoto: int
    textSearch: str
    tagIDs: List[int]
    allowedCategoriesOnly: bool
    objectIDs: List[int]
    brands: List[str]
    imtID: int
