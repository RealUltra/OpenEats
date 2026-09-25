
import os


def test_check_which_directory_is_used():
    active_dir = os.getenv("COSC310_DATA_DIR", "")
    
    assert active_dir != "", "TEST FAILED: No directory was set by the fixture!"
    
    print(f"\n---> THE APP IS USING: {active_dir} FOR TESTING DATA <---\n")
    
    assert "sample-data" not in active_dir, f"TEST FAILED: Danger! It is using the REAL data folder: {active_dir}"

    assert "pytest" in active_dir, f"TEST FAILED: Not in the correct temp dir. Found: {active_dir}"




#Note will fail since the endpoint is not implemented yet, currently gives 404 Not Found
def test_restaurants_endpoint_returns_200(client):
    
    response = client.get("/restaurants")
    assert response.status_code == 200 #Most likely will be 200 OK
    
def test_restaurants_endpoint_returns_valid_json(client):
    response = client.get("/restaurants")
    
    