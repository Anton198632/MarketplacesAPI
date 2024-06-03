from dataclasses import dataclass, field
from typing import Optional

from WB.content.responses.response import Response


@dataclass
class Country:
    name: Optional[str] = field(
        default=None,
        metadata={"description": "Значение характеристики Страны"},
    )
    fullName: Optional[str] = field(
        default=None, metadata={"description": "Полное название страны"},
    )


@dataclass
class ResponseDirectoryCountries(Response):
    data: Optional[Country] = field(
        default=None, metadata={"description": "Объект с информацией о стране"}
    )
