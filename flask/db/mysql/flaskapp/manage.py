# encoding=utf-8

from flask_script import Manager
from flaskapp import app
from models import User

manager = Manager(app)

@manager.command
def save():
    user = User(1, "jikexueyuan01")
    user.save()

@manager.command
def query_all():
    users = User.query_all()
    for u in users:
        print u

if __name__ == '__main__':
    manager.run()