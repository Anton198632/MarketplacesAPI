from dataclasses import dataclass, field
from typing import List


@dataclass
class TagData:
    color: str = field(
        metadata={
            "description": (
                "Цвет тега. Доступные цвета: D1CFD7 - серый, FEE0E0 - красный,"
                " ECDAFF - фиолетовый, E4EAFF - синий, DEF1DD - зеленый,"
                " FFECC7 - желтый"
            ),
        },
    )
    name: str = field(metadata={"description": "Имя тега"})


@dataclass
class TagNomenclatureData:
    nmID: int = field(metadata={"description": "Артикул WB"})
    tagsIDs: List[int] = field(
        metadata={
            "description": (
                "Массив числовых идентификаторов тегов. Чтобы снять теги с КТ,"
                " необходимо передать пустой массив. Чтобы добавить теги к уже"
                " имеющимся в КТ, необходимо в запросе передать новые теги и"
                " теги, которые уже есть в КТ."
            ),
        },
    )

