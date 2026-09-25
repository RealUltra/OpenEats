from fastapi import FastAPI, HTTPException
from json import JSONDecodeError

from backend.app.core.dependencies import get_restaurant_service
from backend.app.schemas.restaurant import Restaurant
from backend.app.services.restaurant_service import RestaurantService

def create_routes(app: FastAPI):
    @app.get("/health")
    async def health():
        return {"status": "ok"}

    @app.get("/restaurants", response_model=list[Restaurant])
    def list_restaurants():
        restaurant_service = get_restaurant_service()

        try:
            return restaurant_service.list_restaurants()

        except JSONDecodeError:
            raise HTTPException(status_code=500, detail="Restaurant data failed to due to invalid JSON")

        except ValueError:
            raise HTTPException(status_code=500, detail="Restaurant data failed to follow correct list[Restaurant] schema")
