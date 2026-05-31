from fastapi import FastAPI

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()


# declare parameters and variables for String 

@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# Path parameters with types for int

@app.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"item_id" : item_id }

# Order matters

@app.get("/user/me")
async def read_user_me():
    return {"user_id": "the current user "}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users")
async def read_user():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]