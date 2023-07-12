from fastapi import FastAPI
from app.api.endpoints import menu, order, user
app = FastAPI()

# include routers to root "/" endpoint from different endpoints.
app.include_router(menu.router)

@app.get("/")
def index():
    return {"message": "Hello World!"}