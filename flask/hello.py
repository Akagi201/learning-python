# -*- coding: utf-8 -*-
#!/usr/bin/env python

# from http://flask.pocoo.org/ tutorial

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route("/hello") # take note of this decorator syntax, it's a common pattern
def hello():
    return "Hello World!"

# variable rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# Unique URLs / Redirection Behavior

# 这种可以兼容url末尾带不带/, 都会用带/的
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
    # app.run()
    app.debug = True
    app.run(host='0.0.0.0')
