from dataclasses import dataclass, field
from typing import Any, Optional, List

from WB.content.responses.card import Card
from WB.content.responses.cursor import Cursor
from WB.content.responses.response import Response


@dataclass
class ResponseTrash(Response):
    data: Optional[Any] = field(default=None)


@dataclass
class CursorTrash(Cursor):
    trashedAt: Optional[str] = field(default=None)


@dataclass
class CardTrash(Card):
    trashedAt: Optional[str] = field(default=None)


@dataclass
class ResponseGetCardsTrash:
    cards: Optional[List[CardTrash]] = field(
        default=None,
        metadata={"description": "Массив карточек товаров"}
    )
    cursor: Optional[CursorTrash] = field(
        default=None,
        metadata={"description": "Пагинатор"}
    )
