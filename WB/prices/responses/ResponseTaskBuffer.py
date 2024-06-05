from WB.prices.schemas import SupplierTaskMetadataBuffer
from dataclasses import dataclass


@dataclass
class ResponseTaskBuffer:
    data: SupplierTaskMetadataBuffer
    error: bool
    errorText: str
