from dataclasses import dataclass


@dataclass
class ContentV2GetCardsTrashRequestSettingsSort:
    #  Сортировать по `trashedAt` (`false` - по убыванию, `true` - по возрастан
    #  ию)
    ascending: bool
