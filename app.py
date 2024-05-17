from flask import Flask, render_template, request, redirect, url_for, session, flash
from auth import load_users, save_user, is_logged_in, current_user, logout
from forms import TaskForm
from models import Task
from models import User
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# def load_users():
#     users = []
#     with open('users.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             users.append(User(row[0], row[1], row[2]))
#     return users

# def save_user(user):
#     users = load_users()
#     if any(existing_user.username == user.username for existing_user in users):
#         return False
#     with open('users.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([user.username, user.password, user.role])
#     return True

# def is_logged_in():
#     return 'username' in session

# def current_user():
#     if 'username' in session:
#         username = session['username']
#         users = load_users()
#         user = next((user for user in users if user.username == username), None)
#         if user:
#             return {'username': username, 'role': user.role}
#     return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if is_logged_in():
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        user = next((user for user in users if user.username == username and user.password == password), None)
        if user:
            session['username'] = user.username
            session['role'] = user.role
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password.'
            return render_template('login.html', error=error)
    return render_template('login.html', is_logged_in=is_logged_in())

@app.route('/register', methods=['GET', 'POST'])
def register():
    if is_logged_in():
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, password)
        if save_user(user):
            return redirect(url_for('login'))
        else:
            error = 'Username already exists.'
    return render_template('register.html', error=error, is_logged_in=is_logged_in())

@app.route('/logout')
def logout_route():
    return logout()
    # session.pop('username', None)
    # return redirect(url_for('login'))

# Hàm load_tasks(): Load danh sách tasks từ file CSV
def load_tasks():
    tasks = []
    with open('tasks.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            task = Task(row['title'], row['description'], row['priority'], row['assigned_to'], row['completed'])
            tasks.append(task)
    return tasks

# Hàm save_tasks(tasks): Lưu danh sách tasks vào file CSV
def save_tasks(tasks):
    with open('tasks.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'description', 'priority', 'assigned_to', 'completed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({'title': task.title, 'description': task.description, 'priority': task.priority, 'assigned_to': task.assigned_to, 'completed': task.completed})

# Route chính, hiển thị danh sách tasks
@app.route('/')
def index():
    if not is_logged_in():
        return redirect(url_for('login'))
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks, is_logged_in=is_logged_in(), current_user=current_user())

# Route thêm task mới
@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    if user and user['role'] != 'admin':
        return redirect(url_for('index'))
    
    users = load_users()

    form = TaskForm()
    form.assigned_to.choices = [(user.username, user.username) for user in users]
    
    if form.validate_on_submit():
        new_task = Task(
                form.title.data,
                form.description.data,
                form.priority.data,
                form.assigned_to.data,
                completed=False,
            )
        print(new_task)
        tasks = load_tasks()
        tasks.append(new_task)
        save_tasks(tasks)
        return redirect(url_for('index'))
    
    # Load danh sách người dùng
    users = load_users()

    return render_template('add_task.html', form=form, users=users, is_logged_in=is_logged_in(), current_user=current_user())

# Route xóa task
@app.route('/delete_task/<int:index>', methods=['GET'])
def delete_task(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    if user and user['role'] == 'admin':
        tasks = load_tasks()
        del tasks[index]
        save_tasks(tasks)
        return redirect(url_for('index'))
    

# Route chỉnh sửa task
@app.route('/edit_task/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    if user and user['role'] != 'admin':
        return redirect(url_for('index'))
    
    print(index)
    tasks = load_tasks()
    task = tasks[index]

    # Load danh sách người dùng
    users = load_users()

    form = TaskForm(obj=task)
    form.assigned_to.choices = [(user.username, user.username) for user in users]
    
    if form.validate_on_submit():
        tasks[index] = Task(form.title.data, form.description.data, form.priority.data, form.assigned_to.data, task.completed)
        save_tasks(tasks)
        return redirect(url_for('index'))
    
    return render_template('edit_task.html', users=users, form=form, is_logged_in=is_logged_in(), current_user=current_user())

# Route hoàn thành task
@app.route('/complete_task/<int:index>', methods=['GET'])
def complete_task(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    tasks = load_tasks()
    current_user = session.get('username')
    if tasks[index].assigned_to != current_user:
        flash("You cannot complete tasks assigned to others.")
        return redirect(request.referrer)
    
    tasks[index].completed = True
    save_tasks(tasks)
    flash("Task completed successfully.")
    return redirect(request.referrer)

@app.route('/not_complete_task/<int:index>', methods=['GET'])
def not_complete_task(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    tasks = load_tasks()
    tasks[index].completed = False
    save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
