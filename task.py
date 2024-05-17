from flask import render_template, request, redirect, url_for, session, flash
from auth import load_users, is_logged_in, current_user
import csv
from forms import TaskForm
from models import Task

def load_tasks():
    tasks = []
    with open('tasks.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            task = Task(row['title'], row['description'], row['priority'], row['assigned_to'], row['completed'])
            tasks.append(task)
    return tasks

def save_tasks(tasks):
    with open('tasks.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'description', 'priority', 'assigned_to', 'completed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({'title': task.title, 'description': task.description, 'priority': task.priority, 'assigned_to': task.assigned_to, 'completed': task.completed})

def index_route():
    if not is_logged_in():
        return redirect(url_for('login'))
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks, is_logged_in=is_logged_in(), current_user=current_user())

def add_task_route():
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
    
    users = load_users()

    return render_template('add_task.html', form=form, users=users, is_logged_in=is_logged_in(), current_user=current_user())

def delete_task_route(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    if user and user['role'] == 'admin':
        tasks = load_tasks()
        del tasks[index]
        save_tasks(tasks)
        return redirect(url_for('index'))
    
def edit_task_route(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    if user and user['role'] != 'admin':
        return redirect(url_for('index'))
    
    print(index)
    tasks = load_tasks()
    task = tasks[index]
    
    users = load_users()

    form = TaskForm(obj=task)
    form.assigned_to.choices = [(user.username, user.username) for user in users]
    
    if form.validate_on_submit():
        tasks[index] = Task(form.title.data, form.description.data, form.priority.data, form.assigned_to.data, task.completed)
        save_tasks(tasks)
        return redirect(url_for('index'))
    
    return render_template('edit_task.html', users=users, form=form, is_logged_in=is_logged_in(), current_user=current_user())

def complete_task_route(index):
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

def not_complete_task_route(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    tasks = load_tasks()
    tasks[index].completed = False
    save_tasks(tasks)
    return redirect(url_for('index'))