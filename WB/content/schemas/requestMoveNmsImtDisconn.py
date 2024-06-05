from dataclasses import dataclass
from typing import List


@dataclass
class requestMoveNmsImtDisconn:
    nmIDs: List[int]
