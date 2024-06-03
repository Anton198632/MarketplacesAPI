from dataclasses import dataclass, field


@dataclass
class BarcodesData:
    count: int = field(
        metadata={
            "description": (
                "Кол-во баркодов которые надо сгенерировать, максимальное"
                " доступное количество баркодов для генерации - `5 000`"
            )
        }
    )
