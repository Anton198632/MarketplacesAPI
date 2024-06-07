from dataclasses import dataclass


@dataclass
class ContentV2CardsUploadRequestVariantsDimensions:
    #  Длина, см
    length: int
    #  Ширина, см
    width: int
    #  Высота, см
    height: int
