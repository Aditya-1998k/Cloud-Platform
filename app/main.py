from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Basic API", version="1.0.0")


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to Basic FastAPI Service"}


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """Get an item by ID"""
    return {"item_id": item_id, "q": q}


@app.post("/items")
def create_item(item: Item):
    """Create a new item"""
    return {"item": item}
