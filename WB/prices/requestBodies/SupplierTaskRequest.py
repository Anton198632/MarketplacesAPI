from WB.prices.schemas import Goods
from dataclasses import dataclass


@dataclass
class SupplierTaskRequest:
    data: Goods
