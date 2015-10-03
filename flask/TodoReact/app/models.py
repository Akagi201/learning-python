from app import db
import datetime


class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default = datetime.datetime.now())
    status = db.IntField(default = 0)

    def to_json(self):
        return {
            'id': str(self.id),
            'content': self.content,
            'time': self.time,
            'status': self.status
        }






