from WB.content.requestBodies import ContentV2GetCardsListRequestSettingsSort
from WB.content.requestBodies import ContentV2GetCardsListRequestSettingsCursor
from WB.content.requestBodies import ContentV2GetCardsListRequestSettingsFilter
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListRequestSettings:
    sort: ContentV2GetCardsListRequestSettingsSort
    filter: ContentV2GetCardsListRequestSettingsFilter
    cursor: ContentV2GetCardsListRequestSettingsCursor
