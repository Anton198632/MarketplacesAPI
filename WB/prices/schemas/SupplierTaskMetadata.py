from WB.prices.schemas import Date1
from WB.prices.schemas import Date
from WB.prices.schemas import TaskStatus
from dataclasses import dataclass


@dataclass
class SupplierTaskMetadata:
    #  ID загрузки
    uploadID: int

    status: TaskStatus

    uploadDate: Date

    activationDate: Date1
    #  Всего товаров
    overAllGoodsNumber: int
    #  Товаров без ошибок
    successGoodsNumber: int
