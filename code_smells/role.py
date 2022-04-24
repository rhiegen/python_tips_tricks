from enum import Enum, auto


class Role(Enum):
    MANAGER = auto()
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()