from WB.prices.schemas import Date
from WB.prices.schemas import Date1
from dataclasses import dataclass
from WB.prices.schemas import TaskStatusBuffer


@dataclass
class SupplierTaskMetadataBuffer:
    uploadID: int
    status: TaskStatusBuffer
    uploadDate: Date
    activationDate: Date1
    overAllGoodsNumber: int
    successGoodsNumber: int
