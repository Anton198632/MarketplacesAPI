from dataclasses import dataclass, field
from typing import List, Optional

from WB.content.responses.response import Response


@dataclass
class Charcs:
    charcID: Optional[int] = field(
        default=None, metadata={"description": "Идентификатор характеристики"}
    )
    subjectName: Optional[str] = field(
        default=None, metadata={"description": "Название предмета"}
    )
    subjectID: Optional[int] = field(
        default=None, metadata={"description": "Идентификатор предмета"}
    )
    name: Optional[str] = field(
        default=None, metadata={"description": "Название характеристики"}
    )
    required: Optional[bool] = field(
        default=None,
        metadata={
            "description": (
                "true - характеристику необходимо обязательно указать в КТ."
                " false - характеристику не обязательно указывать"
            ),
        },
    )
    unitName: Optional[str] = field(
        default=None, metadata={"description": "Единица измерения"}
    )
    maxCount: Optional[int] = field(
        default=None,
        metadata={
            "description": (
                "Максимальное кол-во значений, которое можно присвоить данной"
                " характеристике. Если 0, то нет ограничения."
            ),
        },
    )
    popular: Optional[bool] = field(
        default=None,
        metadata={
            "description": (
                "Характеристика популярна у пользователей"
                " (true - да, false - нет)"
            ),
        },
    )
    charcType: Optional[int] = field(
        default=None,
        metadata={
            "description": (
                "Тип характеристики (1 и 0 - строка или массив строк;"
                " 4 - число или массив чисел)"
            ),
        },
    )


@dataclass
class ResponseObjectCharcs(Response):
    data: List[Charcs] = field(
        default_factory=list, metadata={"description": "Данные"}
    )
