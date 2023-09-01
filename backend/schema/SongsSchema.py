from bson.objectid import ObjectId
import json


def post_SongsSchema(data):
    from config.db import Songs

    data = dict(data)
    Songs.insert_one(data)
    return "Songs successfully added"

def get_SongsData():
    from config.db import Songs
    lst=[]
    data=Songs.find({})
    for item in data:
        # typecasting obj to str
        item["_id"]=str(item["_id"])  
        lst.append(item)
    return lst

def delete_Songs(id):
    from config.db import Songs
    documet=Songs.find_one({"_id":ObjectId(id)})
    if documet:
        Songs.delete_one({"_id":ObjectId(id)})
        return "data has been Deleted"
    else:
        return "invalid SongsId"