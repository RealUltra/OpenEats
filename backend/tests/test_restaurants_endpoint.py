
import os
from pydantic import TypeAdapter
from backend.app.schemas.restaurant import Restaurant

def test_restaurants_endpoint_returns_200(client):
    
    response = client.get("/restaurants")
    assert response.status_code == 200, f"Failed! Server returned: {response.json()}"
    
def test_restaurants_endpoint_returns_valid_json(client):
    response = client.get("/restaurants")
    assert response.status_code == 200, f"Failed! Server returned: {response.json()}"
    data = response.json()
    
    adapter = TypeAdapter(list[Restaurant])
    
    restaurants = adapter.validate_python(data)
    
    assert len(restaurants) > 2, "Expected at least 2 restaurants in the test data"