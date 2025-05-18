from pymongo import MongoClient

import os
from dotenv import load_dotenv

def get_db():
    uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
    client = MongoClient(uri)
    return client["quotesdb"]
