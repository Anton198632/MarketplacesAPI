from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2TagNomenclatureLinkRequest:
    nmID: int
    tagsIDs: List[int]
