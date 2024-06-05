from WB.prices.schemas import Date
from WB.prices.schemas import Date1
from dataclasses import dataclass
from WB.prices.schemas import TaskStatus


@dataclass
class SupplierTaskMetadata:
    uploadID: int
    status: TaskStatus
    uploadDate: Date
    activationDate: Date1
    overAllGoodsNumber: int
    successGoodsNumber: int
