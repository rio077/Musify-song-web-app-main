from bson.objectid import ObjectId
import json


def post_SignUpSchema(data):
    from config.db import SignUp
    data = dict(data)
    SignUp.insert_one(data)
    return "SignUp successfully"

def get_SignUpData():
    from config.db import SignUp
    lst=[]
    data=SignUp.find({})
    for item in data:
        # typecasting obj to str
        item["_id"]=str(item["_id"])  
        lst.append(item)
    return lst

def get_oneSignUp(id):
    from config.db import SignUp
    # typecasting of str to obj
    data=SignUp.find_one({"_id" : ObjectId(id)})
    data["_id"]=str()
    return data

def delete_SignUp(id):
    from config.db import SignUp
    documet=SignUp.find_one({"_id":ObjectId(id)})
    if documet:
        SignUp.delete_one({"_id":ObjectId(id)})
        return "data has been Deleted"
    else:
        return "invalid SignUpId"
