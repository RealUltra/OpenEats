# OpenEats

## Development

### Current Working Directory

**Make sure to run all of the following commands from the root directory i.e OpenEats.**

### Create a virtual environment
```
python -m venv ./backend/.venv 
```

### Activate the virtual environment

**Linux or macOS:** `source ./backend/.venv/bin/activate`

**Windows:** `./backend/.venv/Scripts/activate`

**Windows (Powershell):** If you're using Powershell on Windows, you must run:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` 
before trying to activate the virtual environment. 

### Install the packages

Once you've activated the environment, install the packages into it.

**Linux or macOS:** `python3 -m pip install -r ./backend/requirements.txt`

**Windows:** `python -m pip install -r ./backend/requirements.txt`

### Sample Data

To use the sample data, rename `backend/sample-data` to `backend/data`.

**Linux/macOS:** `mv backend/sample-data backend/data`
**Windows (Command Prompt):** `ren backend/sample-data data`
**Windows (Powershell):** `Rename-Item backend/sample-data backend/data`

### Run the API
```
uv run fastapi dev --entrypoint backend.app.main:main
```


## Testing

To run Pytest on this project:

First, testing data must be added to the test/test-data directory, for easy testing copy the backend/sample-data files into test/test-data.

Then run:
```
python -m pytest backend/tests -q -s --tb=short
```


## Endpoints

- /health
- /restaurants
- /docs