class Task:
    def __init__(self, title, description, priority, assigned_to, completed):
        self.title = title
        self.description = description
        self.priority = priority
        self.assigned_to = assigned_to
        self.completed = completed

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
