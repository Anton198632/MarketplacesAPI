from WB.content.requestBodies import ContentV2CardsUploadRequestVariantsCharacteristics
from WB.content.requestBodies import ContentV2CardsUploadRequestVariantsDimensions
from WB.content.requestBodies import ContentV2CardsUploadRequestVariantsSizes
from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2CardsUploadRequestVariants:
    brand: str
    title: str
    description: str
    vendorCode: str
    dimensions: ContentV2CardsUploadRequestVariantsDimensions
    sizes: List[ContentV2CardsUploadRequestVariantsSizes]
    characteristics: List[ContentV2CardsUploadRequestVariantsCharacteristics]
