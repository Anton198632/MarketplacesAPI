from WB.prices.schemas import Date
from WB.prices.schemas import Date1
from dataclasses import dataclass
from WB.prices.schemas import TaskStatusBuffer


@dataclass
class SupplierTaskMetadataBuffer:
    #  ID загрузки
    uploadID: int

    status: TaskStatusBuffer

    uploadDate: Date

    activationDate: Date1
    #  Всего товаров
    overAllGoodsNumber: int
    #  Товаров без ошибок (0, потому что загрузка в обработке)
    successGoodsNumber: int
