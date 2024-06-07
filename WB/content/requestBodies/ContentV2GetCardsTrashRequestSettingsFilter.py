from dataclasses import dataclass


@dataclass
class ContentV2GetCardsTrashRequestSettingsFilter:
    #  Поиск по артикулу продавца, артикулу WB, баркоду.
    textSearch: str
