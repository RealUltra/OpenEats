from fastapi import FastAPI

def create_routes(app: FastAPI):
    @app.get("/health")
    async def health():
        return {"status": "ok"}
