from fastapi import APIRouter
from app.services.database import get_node, get_nodes

router = APIRouter()

@router.get("/node/{node_id}")
def read_node(node_id: int):
    node = get_node(node_id)
    if not node:
        return {"error": "Not found"}

    children = []
    all_nodes = get_nodes(node[1])
    for n in all_nodes:
        if n[5] == node_id:
            children.append(n[0])

    return {
        "id": node[0],
        "version_id": node[1],
        "heading": node[3],
        "level": node[4],
        "body": node[5] if node[5] else "",
        "children": children,
        "hash": node[6]
    }
