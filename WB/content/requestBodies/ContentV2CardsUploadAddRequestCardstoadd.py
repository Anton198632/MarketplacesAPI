from WB.content.requestBodies import ContentV2CardsUploadAddRequestCardstoaddCharacteristics
from WB.content.requestBodies import ContentV2CardsUploadAddRequestCardstoaddSizes
from typing import List
from WB.content.requestBodies import ContentV2CardsUploadAddRequestCardstoaddDimensions
from dataclasses import dataclass


@dataclass
class ContentV2CardsUploadAddRequestCardstoadd:
    brand: str
    vendorCode: str
    title: str
    description: str
    dimensions: ContentV2CardsUploadAddRequestCardstoaddDimensions
    characteristics: List[ContentV2CardsUploadAddRequestCardstoaddCharacteristics]
    sizes: List[ContentV2CardsUploadAddRequestCardstoaddSizes]
