import os
import shutil
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from backend.app.main import main

CURRENT_DIR = Path(__file__).resolve().parent
REAL_DATA = CURRENT_DIR.parent / "data"
TEST_DATA = CURRENT_DIR.parent / "tests/test-data"

#File must be exactly this name to be known as a pytest fixture file.

@pytest.fixture(autouse=True)
def isolated_data(tmp_path, monkeypatch):
    
    target_file = REAL_DATA / "restaurants.json"
    test_file = TEST_DATA / "restaurants.json"
    
    if not target_file.exists():
        pytest.exit(f"CRITICAL ABORT: Missing required file '{target_file}'. Please add it to the data folder.")
        
    if not test_file.exists():
        pytest.exit(f"CRITICAL ABORT: Missing required test file '{test_file}'. Please create the test-data folder and add restaurants.json.")
    
    #Will have all other files needed to copy for temp use later
    files_to_track = ["restaurants.json"]
    
    for name in files_to_track:
        shutil.copy(REAL_DATA / name, tmp_path / name)
        
    for name in files_to_track:
        shutil.copy(TEST_DATA / name, REAL_DATA / name)
    #Wait until all tests are done
    yield
    
    for name in files_to_track:
        shutil.copy(tmp_path / name, REAL_DATA / name)



@pytest.fixture
def client():
    app = main()
    return TestClient(app)