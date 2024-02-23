from fastapi import APIRouter
from config.db import conn
from fastapi import  Request
from fastapi.responses import HTMLResponse
from schemas.note import noteEntity , notesEntity
from models.note import Note
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
note = APIRouter()

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.keep_notes.notes.find()
    notes_data = []
    for doc in docs:
        notes_data.append(doc)

    return templates.TemplateResponse(request=request, name="item.html" ,context = {"notes_data" : notes_data})


@note.post("/")
async def add_item(request: Request):
    form = await request.form()
    formdict = dict(form)
    conn.keep_notes.notes.insert_one(formdict)
    return {"success" : True}



    
    
    
