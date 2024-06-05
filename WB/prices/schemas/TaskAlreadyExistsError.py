from WB.prices.schemas import TaskAlreadyExistsErrorData
from dataclasses import dataclass


@dataclass
class TaskAlreadyExistsError:
    data: TaskAlreadyExistsErrorData
    error: bool
    errorText: str
