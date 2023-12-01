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
    
# enum example
@app.get("/items/{item_id}")
async def read_item(item_id: userEnum):
    if(item_id == userEnum.efto):
        return {"item_id": item_id}
    return {"item_id": "not efto"}

# query example
local_data = [
    {"id": 1, "name": "efto"},
    {"id": 2, "name": "efto2"},
    {"id": 3, "name": "efto3"}
]


@app.get("/items")
async def get_items(skip: int = 0, limit: int = 10):
    return local_data[skip : skip + limit]
    

