from flask import render_template, request, redirect, url_for, session
import csv
import bcrypt
from models import User

def load_users():
    users = []
    with open('database/users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            users.append(User(row[0], row[1], row[2]))
    return users

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(hashed_password, plain_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def save_user(user):
    users = load_users()
    if any(existing_user.username == user.username for existing_user in users):
        return False
    with open('database/users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user.username, user.password, user.role])
    return True

def is_logged_in():
    return 'username' in session

def current_user():
    if 'username' in session:
        username = session['username']
        users = load_users()
        user = next((user for user in users if user.username == username), None)
        if user:
            return {'username': username, 'role': user.role}
    return None

def logout_route():
    session.pop('username', None)
    return redirect(url_for('login'))

def register_route():
    if is_logged_in():
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)
        user = User(username, hashed_password + 'hcmute')
        if save_user(user):
            return redirect(url_for('login'))
        else:
            error = 'Username already exists.'
    return render_template('register.html', error=error, is_logged_in=is_logged_in())

def login_route():
    if is_logged_in():
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        user = next((user for user in users if user.username == username), None)
        if user and check_password(user.password.replace('hcmute', ''), password):
            session['username'] = user.username
            session['role'] = user.role
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', error=error, is_logged_in=is_logged_in())