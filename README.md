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


### Run the API
```
uv run fastapi dev --entrypoint backend.app.main:main
```