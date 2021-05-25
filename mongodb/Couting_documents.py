import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb

Users = db.users

documents_count = Users.find().count()
print(str(db.name).title() + "'s", Users.name + " has a total of", str(documents_count), "documents in it.")

documents_count_fnumber = Users.find({"favorite_number": 425}).count()
print("And", documents_count_fnumber, "documents with favorite number 425.")
