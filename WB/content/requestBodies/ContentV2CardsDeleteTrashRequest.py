from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2CardsDeleteTrashRequest:
    nmIDs: List[int]
