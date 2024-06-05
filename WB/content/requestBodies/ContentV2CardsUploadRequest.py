from WB.content.requestBodies import ContentV2CardsUploadRequestVariants
from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2CardsUploadRequest:
    subjectID: int
    variants: List[ContentV2CardsUploadRequestVariants]
