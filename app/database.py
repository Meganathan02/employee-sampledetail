from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.employee_db
collection = db.employees