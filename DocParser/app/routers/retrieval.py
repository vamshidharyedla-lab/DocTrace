from fastapi import APIRouter
from app.services.database import get_generated_test
import json

router = APIRouter()

@router.get("/retrieve-tests")
def retrieve_tests(selection_id: int = None):
    if not selection_id:
        return {"error": "selection_id required"}

    row = get_generated_test(selection_id)
    if not row:
        return {"error": "No tests found"}

    tests = json.loads(row[3])
    return {"selection_id": selection_id, "tests": tests, "generated_at": row[5]}
