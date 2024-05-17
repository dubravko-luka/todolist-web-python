from flask import Flask
from auth import logout_route, register_route, login_route
from task import index_route, add_task_route, delete_task_route, edit_task_route, complete_task_route, not_complete_task_route
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_route()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_route()

@app.route('/logout')
def logout():
    return logout_route()

@app.route('/')
def index():
    return index_route()

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    return add_task_route()

@app.route('/delete_task/<int:index>', methods=['GET'])
def delete_task(index):
    return delete_task_route(index) 
    
@app.route('/edit_task/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    return edit_task_route(index)

@app.route('/complete_task/<int:index>', methods=['GET'])
def complete_task(index):
    return complete_task_route(index)

@app.route('/not_complete_task/<int:index>', methods=['GET'])
def not_complete_task(index):
    return not_complete_task_route(index)

if __name__ == '__main__':
    app.run()
