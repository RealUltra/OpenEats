from fastapi import FastAPI

def create_routes(app: FastAPI):
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
