from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/cars/{cars_id}")
async def read_item(cars_id: int, cars_name: str = None):
        if cars_id == 1:
            return {"cars_id": 1, "cars_name": "VW Lupo"}
        else:
            return {"cars_id": cars_id, "cars_name": cars_name}

items = [
]

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item