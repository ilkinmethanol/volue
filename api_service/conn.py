from pymongo import *

cluster = MongoClient("mongodb+srv://ilkinm:Spiderman11A@cluster0.aog30.mongodb.net/volue?retryWrites=true&w=majority")

db = cluster["volue"]
coll = db["customer_data"]

data = {"_id":0, "name":"kele"}

coll.insert_one(data)
