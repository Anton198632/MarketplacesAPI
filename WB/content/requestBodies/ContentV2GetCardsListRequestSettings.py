from WB.content.requestBodies import ContentV2GetCardsListRequestSettingsSort
from WB.content.requestBodies import ContentV2GetCardsListRequestSettingsCursor
from WB.content.requestBodies import ContentV2GetCardsListRequestSettingsFilter
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListRequestSettings:
    #  Параметр сортировки
    sort: ContentV2GetCardsListRequestSettingsSort
    #  Параметры фильтрации
    filter: ContentV2GetCardsListRequestSettingsFilter
    #  Курсор
    cursor: ContentV2GetCardsListRequestSettingsCursor
