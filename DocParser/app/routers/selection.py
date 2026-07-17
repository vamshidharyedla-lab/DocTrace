from fastapi import APIRouter
from app.models import SelectionCreate
from app.services.database import insert_selection, get_selection
from datetime import datetime

router = APIRouter()

@router.post("/selections")
def create_selection(sel: SelectionCreate):
    sel_id = insert_selection(sel.name, sel.node_ids, datetime.now().isoformat())
    return {"id": sel_id, "name": sel.name, "node_ids": sel.node_ids}

@router.get("/selections/{sel_id}")
def read_selection(sel_id: int):
    sel = get_selection(sel_id)
    if not sel:
        return {"error": "Not found"}
    import ast
    return {"id": sel[0], "name": sel[1], "node_ids": ast.literal_eval(sel[2])}
