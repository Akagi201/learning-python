
import pymongo

def get_coll():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.jikexueyuan
    user = db.user_collection

    return user

class User(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        user = {"name": self.name, "email": self.email}
        coll = get_coll()
        id = coll.insert(user)
        print id

    @staticmethod
    def query_users():
        users = get_coll().find()
        return users

    def __str__(self):
        return "id:{}--name:{}".format(self.user_id, self.user_name)


