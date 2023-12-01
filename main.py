from fastapi import FastAPI

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


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items")
async def get_items():
    return {"items": "items"}