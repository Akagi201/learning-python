import wtforms_json
from wtforms import Form
from wtforms.fields import BooleanField, StringField

wtforms_json.init()


class LocationForm(Form):
    name = StringField()
    address = StringField()


class EventForm(Form):
    name = StringField()
    is_public = BooleanField()


json = {
    'name': 'First Event',
    'location': {'name': 'some location'},
}

form = EventForm.from_json(json)

print(form.data)
print(form.patch_data)

# json = {
#     'some_unknown_key': 'some_value'
# }

# Throws exception
# form = EventForm.from_json(json, skip_unknown_keys=False)
