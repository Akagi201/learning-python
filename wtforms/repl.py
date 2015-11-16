from wtforms import Form, StringField, validators


class UsernameForm(Form):
    username = StringField('Username', [validators.Length(min=5)], default=u'test')


form = UsernameForm()
print(form['username'])
print(form.username)
print(form.username.data)

print(form.validate())
print(form.errors)

form2 = UsernameForm(username=u'Robert')
print(form2.data)
print(form2.validate())
print(form2.errors)


class ChangeEmailForm(Form):
    email = StringField('Email', [
        validators.Length(min=6, message=u'Little short for an email address?'),
        validators.Email(message=u'That\'s not a valid email address.')
    ])

class SimpleForm(Form):
    content = StringField('content')

form = SimpleForm(content='foobar')
print(str(form.content))
print(unicode(form.content))
print(form.content(style="width: 200px;", class_="bar"))