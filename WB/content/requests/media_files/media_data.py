from dataclasses import dataclass, field
from typing import List


@dataclass
class MediaSaveData:
    nmId: int
    data: List[str] = field(
        metadata={
            "description": (
                "Ссылки на изображения в том порядке, в котором они будут на"
                " карточке товара"
            ),
        },
    )


@dataclass
class MediaFileData:
    uploadfile: bytes
