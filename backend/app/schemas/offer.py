from decimal import Decimal

from pydantic import BaseModel, Field

from backend.app.schemas.item_availability import ItemAvailability

class Offer(BaseModel):
    type: str = Field("Offer", frozen=True)
    price: Decimal
    priceCurrency: str
    availability: ItemAvailability