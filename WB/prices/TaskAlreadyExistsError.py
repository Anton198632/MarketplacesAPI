from dataclasses import dataclass
from typing import Optional
import TaskAlreadyExistsError_data


@dataclass
class TaskAlreadyExistsError:
    data: TaskAlreadyExistsError_data
    error: bool
    errorText: Optional[str]
