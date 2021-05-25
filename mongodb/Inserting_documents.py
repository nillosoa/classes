import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb

users = db.users
user1 = {"username": "nick", "password": "myverysecurepassword", "favorite_number": 425, "hobbies": ["python", "games", "pizza"]}
user_id = users.insert_one(user1)
print("Nick's id is", user_id.inserted_id)