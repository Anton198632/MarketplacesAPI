from dataclasses import dataclass
from typing import List


@dataclass
class ContentV3MediaSaveRequest:
    nmId: int
    data: List[str]
