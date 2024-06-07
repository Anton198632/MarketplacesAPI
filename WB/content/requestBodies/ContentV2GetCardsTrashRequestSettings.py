from WB.content.requestBodies import (
    ContentV2GetCardsTrashRequestSettingsCursor,
)
from WB.content.requestBodies import (
    ContentV2GetCardsTrashRequestSettingsFilter,
)
from WB.content.requestBodies import ContentV2GetCardsTrashRequestSettingsSort
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsTrashRequestSettings:
    #  Параметр сортировки
    sort: ContentV2GetCardsTrashRequestSettingsSort
    #  Курсор
    cursor: ContentV2GetCardsTrashRequestSettingsCursor
    #  Параметры фильтрации
    filter: ContentV2GetCardsTrashRequestSettingsFilter
