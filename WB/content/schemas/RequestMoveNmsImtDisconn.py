from dataclasses import dataclass
from typing import List


@dataclass
class RequestMoveNmsImtDisconn:
    #  `nmID`, которые необходимо разъединить (max 30)
    nmIDs: List[int]
