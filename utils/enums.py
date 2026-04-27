from enum import Enum


class Sorting(str, Enum):
    LOW_TO_HIGH = "price_asc"
    HIGH_TO_LOW = "price_desc"
