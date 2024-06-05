from WB.content.requestBodies import ContentV2CardsUploadAddRequestCardstoadd
from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2CardsUploadAddRequest:
    imtID: int
    cardsToAdd: List[ContentV2CardsUploadAddRequestCardstoadd]
