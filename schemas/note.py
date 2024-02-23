def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title" : item["title"],
        "notes" : item["notes"]
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]