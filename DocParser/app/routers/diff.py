from fastapi import APIRouter
from app.services.versioning import diff_nodes

router = APIRouter()

@router.get("/diff/node/{node_id}")
def diff_node(node_id: int, from_ver: int, to_ver: int):
    diffs = diff_nodes(from_ver, to_ver)
    for d in diffs:
        if d["node_id"] == node_id:
            return d
    return {"changed": False}
