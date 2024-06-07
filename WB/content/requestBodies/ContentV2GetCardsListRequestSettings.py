from WB.content.requestBodies import ContentV2GetCardsListRequestSettingsSort
from WB.content.requestBodies import ContentV2GetCardsListRequestSettingsFilter
from WB.content.requestBodies import ContentV2GetCardsListRequestSettingsCursor
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListRequestSettings:
    #  Параметр сортировки
    Sort: ContentV2GetCardsListRequestSettingsSort
    #  Параметры фильтрации
    Filter: ContentV2GetCardsListRequestSettingsFilter
    #  Курсор
    Cursor: ContentV2GetCardsListRequestSettingsCursor
