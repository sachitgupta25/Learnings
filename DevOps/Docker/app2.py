# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI APP2!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id_app2": item_id}
