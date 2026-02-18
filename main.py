from fastapi import FastAPI, HTTPException, status
from typing import List
from datetime import datetime
from models import Item, ItemCreate, ItemUpdate

app = FastAPI(title="Tracker Backend")

# In-memory storage
items_db = []
current_id = 0

@app.get("/items", response_model=List[Item])
def list_items():
    """Retrieve a list of all tracked items."""
    return items_db

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    """Create a new item."""
    global current_id
    current_id += 1
    new_item = Item(
        id=current_id,
        title=item.title,
        description=item.description,
        status=item.status,
        created_at=datetime.now()
    )
    items_db.append(new_item)
    return new_item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Retrieve a specific item by its ID."""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemUpdate):
    """Update an existing item."""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            updated_data = item.model_dump()
            update_data = item_update.model_dump(exclude_unset=True)
            updated_data.update(update_data)
            
            updated_item = Item(**updated_data)
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    """Delete an item."""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item not found")
