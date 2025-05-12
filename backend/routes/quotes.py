from flask import Blueprint, jsonify
from random import randint
from backend.db import get_db

quotes_bp = Blueprint('quotes', __name__)
db = get_db()
quotes = db["quotes"]

@quotes_bp.route("/api/quote", methods=["GET"])
def get_quote():
    count = quotes.count_documents({})
    if count == 0:
        return jsonify({"quote": "No quotes found"})
    quote = quotes.find().skip(randint(0, count - 1)).limit(1)[0]
    return jsonify({"quote": quote["text"]})
