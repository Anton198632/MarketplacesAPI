from WB.content.requestBodies import ContentV2CardsUpdateRequestCharacteristics
from WB.content.requestBodies import ContentV2CardsUpdateRequestDimensions
from typing import List
from WB.content.requestBodies import ContentV2CardsUpdateRequestSizes
from dataclasses import dataclass


@dataclass
class ContentV2CardsUpdateRequest:
    nmID: int
    vendorCode: str
    brand: str
    title: str
    description: str
    dimensions: ContentV2CardsUpdateRequestDimensions
    characteristics: List[ContentV2CardsUpdateRequestCharacteristics]
    sizes: List[ContentV2CardsUpdateRequestSizes]
