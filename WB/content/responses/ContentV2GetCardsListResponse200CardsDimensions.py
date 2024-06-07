from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListResponse200CardsDimensions:
    #  Длина, см
    length: int
    #  Ширина, см
    width: int
    #  Высота, см
    height: int
