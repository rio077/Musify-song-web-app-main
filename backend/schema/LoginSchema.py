from bson.objectid import ObjectId
import json


def post_LoginSchema(data):
    from config.db import Login

    data = dict(data)
    Login.insert_one(data)
    return "Login successfully"


def delete_Login(id):
    from config.db import Login
    documet=Login.find_one({"_id":ObjectId(id)})
    if documet:
        Login.delete_one({"_id":ObjectId(id)})
        return "data has been Deleted"
    else:
        return "invalid LoginId"