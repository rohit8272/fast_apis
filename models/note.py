from pydantic import BaseModel

class Note(BaseModel):
    id:   str
    title: str
    notes: str