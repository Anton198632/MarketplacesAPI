from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListRequestSettingsCursor:
    #  Сколько КТ выдать в ответе.
    limit: int
