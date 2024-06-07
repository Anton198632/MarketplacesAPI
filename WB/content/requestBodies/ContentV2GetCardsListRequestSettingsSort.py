from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListRequestSettingsSort:
    #  Сортировать по полю **updatedAt** (`false` - по убыванию, `true` - по во
    #  зрастанию)
    ascending: bool
