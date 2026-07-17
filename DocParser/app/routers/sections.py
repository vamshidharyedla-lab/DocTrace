from fastapi import APIRouter
from app.services.database import get_nodes

router = APIRouter()

@router.get("/sections")
def list_sections(version_id: int = None):
    nodes = get_nodes(version_id)
    sections = []
    for n in nodes:
        if n[4] == 1:
            sections.append({"id": n[0], "heading": n[3], "level": n[4]})
    return sections
