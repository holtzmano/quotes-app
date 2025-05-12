from backend.db import get_db

db = get_db()
quotes = db["quotes"]

quotes.delete_many({})
quotes.insert_many([
    {"text": "Believe in yourself."},
    {"text": "Dream big, work hard."},
    {"text": "Never give up."},
    {"text": "Push beyond limits."}
])

print("✅ Seeded quotes into MongoDB.")
