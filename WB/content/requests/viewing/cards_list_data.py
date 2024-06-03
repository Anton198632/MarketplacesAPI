from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Sort:
    ascending: bool = field(
        default=True,
        metadata={
            "description": (
                "Сортировать по полю **updatedAt** (`false` - по убыванию,"
                " `true` - по возрастанию)"
            )
        }
    )


@dataclass
class Filter:
    withPhoto: Optional[int] = field(
        default=None,
        metadata={
            "description": (
                "Фильтр по фото:\n\n* `0` — только карточки без фото\n*"
                " `1` — только карточки с фото\n* `-1` — все карточки товара"
            )
        },
    )
    textSearch: Optional[str] = field(
        default=None,
        metadata={
            "description": "Поиск по артикулу продавца, артикулу WB, баркоду",
        }
    )
    tagIDs: Optional[List[int]] = field(
        default=None, metadata={"description": "Поиск по ID тегов"},
    )
    allowedCategoriesOnly: Optional[bool] = field(
        default=None,
        metadata={
            "description": (
                "Фильтр по категории. `True` - только разрешённые,"
                " `False` - все. Не используется в песочнице."
            ),
        },
    )
    objectIDs: Optional[List[int]] = field(
        default=None, metadata={"description": "Поиск по id предметов"},
    )
    brands: Optional[List[str]] = field(
        default=None, metadata={"description": "Поиск по брендам"},
    )
    imtID: Optional[int] = field(
        default=None, metadata={"description": "Поиск по идентификатору КТ"},
    )


@dataclass
class Cursor:
    limit: int = field(
        default=10, metadata={"description": "Сколько КТ выдать в ответе."}
    )


@dataclass
class Settings:
    sort: Sort = field(
        default=Sort, metadata={"description": "Параметры сортировки"}
    )
    filter: Filter = field(
        default=Filter, metadata={"description": "Параметры фильтрации"}
    )
    cursor: Cursor = field(default=Cursor, metadata={"description": "Курсор"})


@dataclass
class CardsListData:
    settings: Settings = field(
        default=Settings, metadata={"description": "Настройки"}
    )
