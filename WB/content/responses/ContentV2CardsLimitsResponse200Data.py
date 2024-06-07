from dataclasses import dataclass


@dataclass
class ContentV2CardsLimitsResponse200Data:
    #  Количество бесплатных лимитов
    freeLimits: int
    #  Количество оплаченных лимитов
    paidLimits: int
