from fastapi import APIRouter
from app.services.database import search_nodes

router = APIRouter()

@router.get("/search")
def search(q: str):
    nodes = search_nodes(q)
    results = []
    for n in nodes:
        results.append({
            "id": n[0],
            "heading": n[3],
            "level": n[4],
            "body": n[5] if n[5] else ""
        })
    return results
