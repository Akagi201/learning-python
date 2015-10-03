from app import app
from app.models import Todo
from flask.ext.script import Manager


manager = Manager(app)


@manager.command
def save():
    todo = Todo(content="study flask")
    todo.save()


if __name__ == '__main__':
    manager.run()