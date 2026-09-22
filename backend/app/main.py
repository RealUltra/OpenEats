from fastapi import FastAPI
from app.api.routes import create_routes

def main():
    app = FastAPI()

    # Add all the routes in app.api.routes
    create_routes(app)

    return app
