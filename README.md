# OpenEats

## Development

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

### Run the API
```
uv run fastapi dev --entrypoint backend.app.main:main
```


## Testing

To run pytest on this project run:

```
python -m pytest -q
```

This automatically runs all tests with temp data that does not affect the orignal