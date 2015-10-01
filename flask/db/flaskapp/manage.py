from flask_script import Manager
from flaskapp import app

manager = Manager(app)

# python manage.py hello
@manager.command
def hello():
    print("hello world")

# python manage.py hello_world -m jikexueyuan
@manager.option('-m', '--msg', dest='msg_val', default='world')
def hello_world(msg_val):
    print("hello "+msg_val)

if __name__ == "__main__":
    manager.run()
