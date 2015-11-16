from wtforms import Form, BooleanField, StringField, validators


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])


class ProfileForm(Form):
    birthday = DateTimeField('Your Birthday', format='%m/%d/%y')
    signature = TextAreaField('Forum Signature')


class AdminProfileForm(ProfileForm):
    username = StringField('Username', [validators.Length(max=40)])
    level = IntegerField('User Level', [validators.NumberRange(min=0, max=10)])
