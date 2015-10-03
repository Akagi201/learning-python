from app import app
from flask import render_template,request, jsonify
from app.models import Todo
from datetime import datetime


@app.route('/')
def index():
    return render_template("index.html")


# add delete update list

@app.route('/add', methods=['POST',])
def add():
    form = request.form
    content = form.get('content')
    todo = Todo(content=content,time=datetime.now())
    todo.save()
    return jsonify(status="success")


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    return jsonify(status="success")


@app.route('/update', methods=['POST',])
def update():
    form = request.form
    todo_id = form.get('id')
    status = form.get('status')
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = status
    todo.save()
    return jsonify(status="success")

@app.route('/list')
def list():
    todos = Todo.objects.order_by('-time')
    return jsonify(status="success", todos=[todo.to_json() for todo in todos])


