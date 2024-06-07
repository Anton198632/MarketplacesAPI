from WB.prices.schemas import SizeGoodsBody
from dataclasses import dataclass


@dataclass
class SupplierTaskRequestSize:

    data: SizeGoodsBody
