import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb

Users = db.users

nick_count = Users.find({"username": "nick"}).count()
print(str(nick_count) + " people named nick(lowercase) in the database.")

nick_count = Users.find({"username": "nick", "favorite_number": 425}).count()
print(str(nick_count) + " people named nick with 425 as favorite number.")