from pathlib import Path

from dotenv import load_dotenv

from backend.app.services.restaurant_service import RestaurantService
load_dotenv()

import os

from backend.app.repositories.restaurant_repository import RestaurantRepository

OPENEATS_DATA_DIR = os.getenv("OPENEATS_DATA_DIR", "")

def get_restaurant_service():
    restaurant_repository = RestaurantRepository(Path(OPENEATS_DATA_DIR) / "restaurants.json")
    return RestaurantService(restaurant_repository)