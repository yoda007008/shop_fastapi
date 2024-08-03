from fastapi import FastAPI
from app.routers import category

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerse app"}

app.include_router(category.router)
