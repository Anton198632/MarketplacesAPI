from dataclasses import dataclass
import TaskCreated_data
from typing import Optional


@dataclass
class TaskCreated:
    data: TaskCreated_data
    error: bool
    errorText: Optional[str]
