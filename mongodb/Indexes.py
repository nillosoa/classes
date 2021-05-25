import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb

index = db.users.create_index([("username", pymongo.ASCENDING)])

for user in db.users.find({"username": "nick"}):
    print(user["username"] + "({})'s".format(user["_id"]), "favorite number is " + str(user["favorite_number"]) + ".")