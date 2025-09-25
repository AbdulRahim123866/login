from enum import Enum


class SeatsStatus(Enum):
    AVAILABLE="available"
    RESERVED="reserved"

class BookStatus(Enum):
    USED="used"
    NEW="new"