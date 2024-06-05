from WB.content.requestBodies import ContentV2GetCardsListRequestSettings
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListRequest:
    settings: ContentV2GetCardsListRequestSettings
