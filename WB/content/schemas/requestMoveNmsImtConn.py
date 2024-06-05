from dataclasses import dataclass
from typing import List


@dataclass
class requestMoveNmsImtConn:
    targetIMT: int
    nmIDs: List[int]
