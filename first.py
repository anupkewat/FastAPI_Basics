from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand : Optional[str] = None

inventory = { }


@app.get('/item/{item_id}')
def get_item(item_id:int = Path(description = 'the ID of the item you want to view', lt = 3,)):
    return inventory[item_id]


@app.get('/get-by-name')
def get_by_name(name : str):
    for item_id in inventory: 
        if inventory[item_id].name == name:
            return inventory[item_id]
    return { 'error' : 'data not found'}

@app.post('/create-item')
def create_item(item_id :int, item : Item):
    if item_id in inventory: 
        return { 'error' : 'item already exists with given item_id'}
    inventory[item_id] = item # FAST API can manage the object directly
    return inventory[item_id]


