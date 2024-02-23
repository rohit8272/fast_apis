from fastapi import FastAPI , Request ,HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.router import note
from config.db import conn
from models.note import Note

app = FastAPI()
app.include_router(note)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# @app.delete("/delete/{_id}" , response_model= Note)
# async def delete_data( _id : str):
#     docs = await conn.keep_notes.notes.find_one_and_delete({"_id" : _id})
#     return {"delete" : True}

# @app.get("/items/{item_id}", response_model=Note)
# async def read_item(item_id: str):
#     item = await conn.keep_notes.notes.find_one({"_id": item_id})
#     if item:
#         return item
#     raise HTTPException(status_code=404, detail="Item not found")

# @app.delete("/items/{item_id}", response_model=Note)
# async def delete_item(item_id: str):
#     deleted_item = await conn.keep_notes.notes.find_one_and_delete({"_id": item_id})
#     if deleted_item:
#         return deleted_item
#     raise HTTPException(status_code=404, detail="Item not found")