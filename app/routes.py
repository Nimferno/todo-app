from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Todo
from app import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template('index.html', todo_list=todo_list)

@main.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    new_todo = Todo(title=title, description=description, completed=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.index'))