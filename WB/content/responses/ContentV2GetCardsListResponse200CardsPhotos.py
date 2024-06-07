from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListResponse200CardsPhotos:
    #  URL фото `900х1200`
    big: str
    #  URL фото `248х328`
    c246x328: str
    #  URL фото `516х688`
    c516x688: str
    #  URL фото `600х600`
    square: str
    #  URL фото `75х100`
    tm: str
