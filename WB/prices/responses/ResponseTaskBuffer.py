from WB.prices.schemas import SupplierTaskMetadataBuffer
from dataclasses import dataclass


@dataclass
class ResponseTaskBuffer:
    """
    Состояние загрузки

    
    """

    data: SupplierTaskMetadataBuffer
    #  Флаг ошибки
    error: bool
    #  Текст ошибки
    errorText: str
