from app.services.database import init_db
from app.services.parser import parse_and_store

init_db()

parse_and_store("data/ct200_manual.pdf", "CT200 Manual", 1)
parse_and_store("data/ct200_manual_v2.pdf", "CT200 Manual", 2)

print("Database seeded with 2 versions")
