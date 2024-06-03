from dataclasses import dataclass, field
from typing import List


@dataclass
class Image:
    url: str


@dataclass
class MediaSaveData:
    nmId: int
    data: List[Image] = field(
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
