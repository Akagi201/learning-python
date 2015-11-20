from flask import Flask, render_template
from flask_wtf import Form
from wtforms import RadioField


SECRET_KEY = 'development'

app = Flask(__name__)
app.config.from_object(__name__)


class SimpleForm(Form):
    example = RadioField('Label', choices=[('value', 'description'), ('value_two', 'whatever')])


@app.route('/', methods=['post', 'get'])
def hello_world():
    form = SimpleForm()
    if form.validate_on_submit():
        print form.example.data
    else:
        print form.errors
    return render_template('example.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
