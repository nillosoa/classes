import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb
Users = db.users

current_date = datetime.datetime.now()
old_date = datetime.datetime(2009, 8, 11)

#uid = Users.insert_one({"username": "ffie", "date": current_date})
#print(uid.inserted_id, "created just now.")

#Mongo's
#$gt = greater than, $gte = greater than or equal to
#$lt = less than, $lte = less than or equal to
#$ne = not equal
gt_old_date = Users.find({"date": {"$gt": old_date}}).count()
lt_old_date = Users.find({"date": {"$lt": old_date}}).count()
ne_nick = Users.find({"date": {"$ne": "nick"}}).count()
users_with_date = Users.find({"date": {"$exists": True}}).count()

print(str(lt_old_date), "documents dated before", str(old_date.year) + "/" + str(old_date.month) + "/" + str(old_date.day) + ".")
print(str(gt_old_date), "documents dated after ", str(old_date.year) + "/" + str(old_date.month) + "/" + str(old_date.day) + ".")
print(str(users_with_date), "total users where the 'date' column was found.")

print()
print(str(ne_nick), "users not named nick.")
