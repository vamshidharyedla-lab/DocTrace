from pydantic import BaseModel
from typing import List, Optional

class Node(BaseModel):
    id: int
    version_id: int
    heading: str
    level: int
    body: str
    parent_id: Optional[int]
    hash: str

class SelectionCreate(BaseModel):
    name: str
    node_ids: List[int]

class Selection(BaseModel):
    id: int
    name: str
    node_ids: List[int]

class TestCase(BaseModel):
    name: str
    steps: List[str]
    expected: str

class GeneratedTest(BaseModel):
    id: int
    selection_id: int
    version_id: int
    tests: List[TestCase]
    prompt: str
    generated_at: str
    stale: bool = False
