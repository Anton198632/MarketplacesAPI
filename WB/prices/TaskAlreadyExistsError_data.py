from dataclasses import dataclass
from typing import Optional


@dataclass
class TaskAlreadyExistsError_data:
    id: Optional[int]
    alreadyExists: bool
