from dataclasses import dataclass
from typing import Optional


@dataclass
class TaskCreated_data:
    id: Optional[int]
    alreadyExists: bool
