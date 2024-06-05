from WB.prices.responses import ResponseSizeListsData
from dataclasses import dataclass


@dataclass
class ResponseSizeLists:
    data: ResponseSizeListsData
    error: bool
    errorText: str
