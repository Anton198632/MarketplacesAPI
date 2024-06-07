from dataclasses import dataclass


@dataclass
class ContentV2CardsUploadAddRequestCardsToAddDimensions:
    #  Длина, см
    length: int
    #  Ширина, см
    width: int
    #  Высота, см
    height: int
