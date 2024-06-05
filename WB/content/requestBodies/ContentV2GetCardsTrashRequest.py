from WB.content.requestBodies import ContentV2GetCardsTrashRequestSettings
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsTrashRequest:
    settings: ContentV2GetCardsTrashRequestSettings
