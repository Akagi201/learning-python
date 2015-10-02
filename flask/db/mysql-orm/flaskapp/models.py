
from flaskapp import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def __str__(self):
        return "id:{}--name:{}".format(self.user_id, self.user_name)


