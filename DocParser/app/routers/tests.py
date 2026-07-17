from fastapi import APIRouter
from app.services.llm import generate_tests
from app.services.database import get_selection, get_node, insert_generated_test, get_generated_test
from app.services.utils import sha256
from datetime import datetime
import json

router = APIRouter()

@router.post("/generate-tests")
def generate_tests_endpoint(selection_id: int):
    sel = get_selection(selection_id)
    if not sel:
        return {"error": "Selection not found"}

    import ast
    node_ids = ast.literal_eval(sel[2])

    texts = []
    hashes = {}
    version_id = None

    for nid in node_ids:
        node = get_node(nid)
        if node:
            version_id = node[1]
            text = node[3] if node[3] else node[5]
            texts.append(text)
            hashes[nid] = node[6]

    tests = generate_tests(texts)
    tests_json = json.dumps(tests)
    prompt = "Generate tests for: " + " ".join(texts)

    test_id = insert_generated_test(selection_id, version_id, tests_json, prompt, datetime.now().isoformat(), json.dumps(hashes))

    return {"id": test_id, "tests": tests}

@router.get("/tests/{selection_id}")
def get_tests(selection_id: int):
    row = get_generated_test(selection_id)
    if not row:
        return {"error": "No tests found"}

    import ast
    tests = json.loads(row[3])
    old_hashes = json.loads(row[6])

    stale = False
    stale_nodes = []

    for nid, old_hash in old_hashes.items():
        node = get_node(int(nid))
        if node and node[6] != old_hash:
            stale = True
            stale_nodes.append(int(nid))

    return {
        "id": row[0],
        "selection_id": row[1],
        "tests": tests,
        "stale": stale,
        "stale_nodes": stale_nodes,
        "generated_at": row[5]
    }
