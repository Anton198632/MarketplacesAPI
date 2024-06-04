from dataclasses import dataclass
from typing import List, Dict, Optional, Union


@dataclass
class Body:
    type: str
    data: List[Dict]


@dataclass
class ItemAPI:
    server: str
    url: str
    method: str
    title: str
    description: str
    body: Optional[Body]
    parameters: Optional[List]
    responses: Union[Dict, str, None]


@dataclass
class API:
    responses: List[ItemAPI]
