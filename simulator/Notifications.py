from enum import Enum
from dataclasses import dataclass


class Status(Enum):
    RETIRE = 0
    PENDING = 1


@dataclass
class Notification:
    status: Status
    author: object
    recipient: object
    callback: function
