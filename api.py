from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int | None


@app.get("/item")
def get_item():
    return Item(name="item1", price=None)
