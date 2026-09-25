from fastapi import FastAPI, Depends

from backend.app.core.dependencies import get_restaurant_service
from backend.app.schemas.restaurant import Restaurant
from backend.app.services.restaurant_service import RestaurantService

def create_routes(app: FastAPI):
    @app.get("/health")
    async def health():
        return {"status": "ok"}

    @app.get("/restaurants", response_model=list[Restaurant])
    async def list_restaurants(restaurant_service: RestaurantService = Depends(get_restaurant_service),):
        return restaurant_service.list_restaurants()