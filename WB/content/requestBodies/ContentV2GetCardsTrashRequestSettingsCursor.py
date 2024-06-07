from dataclasses import dataclass


@dataclass
class ContentV2GetCardsTrashRequestSettingsCursor:
    #  Сколько КТ выдать в ответе
    limit: int
