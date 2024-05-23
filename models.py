import datetime

class Task:
    def __init__(self, id, title, description, priority, category, created_by, completed, progress = 0, created_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.category = category
        self.created_by = created_by
        self.completed = completed
        self.progress = progress
        self.created_date = created_date or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role

class Category:
    def __init__(self, id, name, created_by):
        self.id = id
        self.name = name
        self.created_by = created_by