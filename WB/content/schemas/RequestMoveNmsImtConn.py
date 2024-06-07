from dataclasses import dataclass
from typing import List


@dataclass
class RequestMoveNmsImtConn:
    #  Существующий у продавца `imtID`, под которым необходимо объединить НМ
    targetIMT: int
    #  `nmID`, которые необходимо объединить (максимум 30)
    nmIDs: List[int]
