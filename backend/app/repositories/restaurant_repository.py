from pathlib import Path
import json
from json import JSONDecodeError
from pydantic import TypeAdapter, ValidationError

from backend.app.schemas.restaurant import Restaurant

restaurants_list_adapter = TypeAdapter(list[Restaurant])

class RestaurantRepository:
    def __init__(self, restaurants_file_path: Path) -> None:
        self.restaurants_file_path: Path = restaurants_file_path

    def __load_restaurants(self) -> list[Restaurant]: 
        if not self.restaurants_file_path.exists():
            print(f"[WARNING] '${self.restaurants_file_path.absolute()}' does not exist. Defaulting to empty restaurants list.")
            return []

        with open(self.restaurants_file_path, "r", encoding="utf-8") as restaurants_file:
            try:
                return restaurants_list_adapter.validate_python(json.load(restaurants_file))
            except JSONDecodeError:
                raise Exception(f"{self.restaurants_file_path.absolute()} is not JSON serializable.")
            except ValidationError:
                raise Exception(f"{self.restaurants_file_path.absolute()} does not follow the correct list[Restaurant] schema. See backend/app/schemas/Restaurant.py or visit https://www.schema.org/Restaurant for schema specifications.")

    def get_all_restaurants(self) -> list[Restaurant]:
        return self.__load_restaurants()