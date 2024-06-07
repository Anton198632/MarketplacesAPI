from WB.content.requestBodies import (
    ContentV2GetCardsTrashRequestSettingsFilter,
)
from WB.content.requestBodies import ContentV2GetCardsTrashRequestSettingsSort
from dataclasses import dataclass
from WB.content.requestBodies import (
    ContentV2GetCardsTrashRequestSettingsCursor,
)


@dataclass
class ContentV2GetCardsTrashRequestSettings:
    #  Параметр сортировки
    Sort: ContentV2GetCardsTrashRequestSettingsSort
    #  Курсор
    Cursor: ContentV2GetCardsTrashRequestSettingsCursor
    #  Параметры фильтрации
    Filter: ContentV2GetCardsTrashRequestSettingsFilter
