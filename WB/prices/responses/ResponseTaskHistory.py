from WB.prices.schemas import SupplierTaskMetadata
from dataclasses import dataclass


@dataclass
class ResponseTaskHistory:
    data: SupplierTaskMetadata
    error: bool
    errorText: str
