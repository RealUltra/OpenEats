from pathlib import Path
import json
from pydantic import TypeAdapter

from backend.app.schemas.restaurant import Restaurant

restaurants_list_adapter = TypeAdapter(list[Restaurant])

class RestaurantRepository:
    def __init__(self, restaurants_file_path: Path) -> None:
        self.restaurants_file_path: Path = restaurants_file_path

    def __load_restaurants(self) -> list[Restaurant]: 
        if not self.restaurants_file_path.exists():
            return []

        with open(self.restaurants_file_path, "r") as restaurants_file:
            restaurants_list = json.load(restaurants_file)
            return restaurants_list_adapter.validate_python(restaurants_list)

    def get_all_restaurants(self) -> list[Restaurant]:
        return self.__load_restaurants()