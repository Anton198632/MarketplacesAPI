from dataclasses import dataclass, field
from typing import List


@dataclass
class NMIDJoinData:
    targetIMT: int = field(
        metadata={
            "description": (
                "Существующий у продавца `imtID`, под которым необходимо"
                " объединить НМ"
            )
        }
    )
    nmIDs: List[int] = field(
        default_factory=list,
        metadata={
            "description": (
                "`nmID`, которые необходимо объединить (максимум 30)"
            )
        }
    )


@dataclass
class NMIDSplitData:
    nmIDs: List[int] = field(
        metadata={
            "description": "`nmID`, которые необходимо разъединить (max 30)"
        }
    )
