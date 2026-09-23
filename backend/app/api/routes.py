from fastapi import FastAPI

def create_routes(app: FastAPI):
    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.get("/health")
    async def health():
        return {"status": "ok"}
