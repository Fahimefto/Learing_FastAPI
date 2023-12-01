from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put("/")
async def rootPut():
    return {"message": "Hello World PUT"}

@app.post("/")
async def rootPost():
    return {"message": "Hello World POST"}

@app.delete("/")
async def rootDelete():
    return {"message": "Hello World DELETE"}

class userEnum(str, Enum):
    efto = "efto"
    efto2 = "efto2"
    efto3 = "efto3"
    

@app.get("/items/{item_id}")
async def read_item(item_id: userEnum):
    if(item_id == userEnum.efto):
        return {"item_id": item_id}
    return {"item_id": "not efto"}

@app.get("/items")
async def get_items():
    return {"items": "items"}

