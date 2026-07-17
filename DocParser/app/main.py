from fastapi import FastAPI
from app.services.database import init_db
from app.routers import sections, nodes, search, diff, selection, tests, retrieval

app = FastAPI(title="DocQA System")

app.include_router(sections.router)
app.include_router(nodes.router)
app.include_router(search.router)
app.include_router(diff.router)
app.include_router(selection.router)
app.include_router(tests.router)
app.include_router(retrieval.router)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"message": "DocQA API"}
