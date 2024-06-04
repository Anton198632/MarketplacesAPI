from dataclasses import dataclass
from typing import Optional


@dataclass
class SupplierTaskMetadataBuffer:
    uploadID: Optional[int]
    status: None
    uploadDate: None
    activationDate: None
    overAllGoodsNumber: Optional[int]
    successGoodsNumber: Optional[int]
