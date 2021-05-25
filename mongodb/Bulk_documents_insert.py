import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb

users = db.users
users_to_insert = [{"username": "Third", "password": "thirdPassword"},
         {"username": "Fourth", "password": "Fourth'sP@ssWord"},
         {"username": "red", "password": "blue"}
         ]

inserted = users.insert_many(users_to_insert)
for item in range(len(users_to_insert)):
    print(users_to_insert[item]["username"] + "'s ID is", inserted.inserted_ids[item])

