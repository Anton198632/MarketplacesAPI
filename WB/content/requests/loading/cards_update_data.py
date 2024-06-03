from dataclasses import dataclass, field

from WB.content.requests.card import Card


@dataclass
class Product(Card):
    nmID: int = field(default=None, metadata={"description": "Артикул WB"})
