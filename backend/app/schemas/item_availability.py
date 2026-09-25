from enum import StrEnum


class ItemAvailability(StrEnum):
    IN_STOCK = "https://schema.org/InStock"
    OUT_OF_STOCK = "https://schema.org/OutOfStock"