import os
import shutil
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from backend.app.main import main

CURRENT_DIR = Path(__file__).resolve().parent
REAL_DATA = CURRENT_DIR.parent / "data"

#File must be exactly this name to be known as a pytest fixture file.

@pytest.fixture(autouse=True)
def isolated_data(tmp_path, monkeypatch):
    
    target_file = REAL_DATA / "restaurants.json"
    if not target_file.exists():
        pytest.exit(f"CRITICAL ABORT: Missing required file '{target_file}'. Please add it to the data folder.")
    
    #Will have all other files needed to copy for temp use later
    for name in ["restaurants.json"]:
        shutil.copy(REAL_DATA / name, tmp_path / name)
    monkeypatch.setenv("COSC310_DATA_DIR", str(tmp_path))
    
    
    #Safety check to make sure we are using temp data
    active_dir = os.getenv("COSC310_DATA_DIR", "")
    
    if "sample-data" in active_dir or "pytest" not in active_dir:
        pytest.exit(f"CRITICAL SAFETY ABORT: Tests are using the wrong directory: {active_dir}")



@pytest.fixture
def client():
    app = main()
    return TestClient(app)