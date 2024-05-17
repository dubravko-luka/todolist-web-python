from flask import session
import csv
from models import User

def load_users():
    users = []
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            users.append(User(row[0], row[1], row[2]))
    return users

def save_user(user):
    users = load_users()
    if any(existing_user.username == user.username for existing_user in users):
        return False
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user.username, user.password, user.role])
    return True

def is_logged_in():
    return 'username' in session