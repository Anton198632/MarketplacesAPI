from dataclasses import dataclass, field
from typing import Optional

from WB.content.responses.response import Response


@dataclass
class LimitsModel:
    freeLimits: Optional[int] = field(
        default=None, metadata={"description": "Количество бесплатных лимитов"}
    )
    paidLimits: Optional[int] = field(
        default=None, metadata={"description": "Количество оплаченных лимитов"}
    )


@dataclass
class ResponseCardsLimits(Response):
    data: LimitsModel = field(
        default=LimitsModel, metadata={"description": "Лимиты по КТ"}
    )
