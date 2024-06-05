from dataclasses import dataclass
from WB.prices.schemas import TaskCreatedData


@dataclass
class TaskCreated:
    data: TaskCreatedData
    error: bool
    errorText: str
