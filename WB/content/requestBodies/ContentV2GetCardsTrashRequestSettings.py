from WB.content.requestBodies import ContentV2GetCardsTrashRequestSettingsFilter
from WB.content.requestBodies import ContentV2GetCardsTrashRequestSettingsCursor
from WB.content.requestBodies import ContentV2GetCardsTrashRequestSettingsSort
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsTrashRequestSettings:
    sort: ContentV2GetCardsTrashRequestSettingsSort
    cursor: ContentV2GetCardsTrashRequestSettingsCursor
    filter: ContentV2GetCardsTrashRequestSettingsFilter
