from dataclasses import dataclass, field
from typing import List, Optional
from uuid import UUID

from WB.content.responses.card import Card
from WB.content.responses.cursor import Cursor
from WB.content.responses.tag import Tag


@dataclass
class CursorCardList(Cursor):
    updatedAt: Optional[str] = field(
        default=None,
        metadata={
            "description": (
                "Дата с которой надо запрашивать следующий список КТ"
            )
        }
    )


@dataclass
class CardData(Card):
    imtID: Optional[int] = field(
        default=None,
        metadata={
            "description": (
                "Идентификатор КТ. Артикулы WB из одной КТ будут иметь"
                " одинаковый imtID"
            )
        }
    )
    nmUUID: Optional[UUID] = field(
        default=None,
        metadata={
            "description": "Внутренний технический идентификатор товара"
        },
    )
    brand: Optional[str] = field(
        default=None, metadata={"description": "Бренд"}
    )
    title: Optional[str] = field(
        default=None, metadata={"description": "Наименование товара"}
    )
    updatedAt: Optional[str] = field(
        default=None, metadata={"description": "Дата изменения"}
    )
    tags: List[Tag] = field(
        default_factory=list, metadata={"description": "Теги"}
    )


@dataclass
class ResponseCardList:
    cards: List[CardData] = field(
        default_factory=list, metadata={"description": "Список КТ"}
    )
    cursor: Optional[CursorCardList] = field(
        default=None, metadata={"description": "Пагинатор"}
    )
