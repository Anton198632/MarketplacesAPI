from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListResponse200Cursor:
    #  Дата с которой надо запрашивать следующий список КТ
    updatedAt: str
    #  Номер Артикула WB с которой надо запрашивать следующий список КТ
    nmID: int
    #  Кол-во возвращенных КТ
    total: int
