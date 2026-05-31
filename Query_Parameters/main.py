from fastapi import FastAPI

app = FastAPI()

# Query Parameters
# URL http://127.0.0.1:8000/items/?skip=0&limit=10
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/item/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
    
# Optional parameters

@app.get("/items/{items_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# Query parameters type conversion
@app.get("/itemss/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"descripation": "This is an amazing item that has a long description"}
        )
    return item
