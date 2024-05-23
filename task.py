from flask import render_template, request, redirect, url_for, session, flash
from auth import load_users, is_logged_in, current_user
from category import load_user_categories
import csv
from forms import TaskForm
from models import Task
from utils import generate_id

def load_tasks():
    tasks = []
    with open('database/tasks.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            task = Task(
                row['id'],
                row['title'],
                row['description'],
                row['priority'],
                row['category'],
                row['created_by'],
                row['completed'],
                int(row['progress']),
                row['created_date'],
            )
            tasks.append(task)
    return tasks

def save_tasks(tasks):
    with open('database/tasks.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'description', 'priority', 'category', 'created_by', 'completed', 'progress', 'created_date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'priority': task.priority,
                'category': task.category,
                'created_by': task.created_by,
                'completed': task.completed,
                'progress': task.progress,
                'created_date': task.created_date
            })

def load_user_tasks():
    user = current_user()
    username = user['username']
    tasks = load_tasks()
    return [task for task in tasks if task.created_by == username]

def index_route():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    categories = load_user_categories(user['username'])
    tasks = load_user_tasks()
    category_filter = request.args.get('category')
    detail_index = request.args.get('detail')
    
    if category_filter:
        tasks = [task for task in tasks if task.category == category_filter]
    else:
        tasks = []

    detail_task = None
    if detail_index:
        detail_task = next((task for task in tasks if int(task.id) == int(detail_index)), None)
        
    return render_template('index.html', tasks=tasks, detail_task=detail_task, is_logged_in=is_logged_in(), current_user=current_user(), categories=categories)

def add_task_route():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    
    users = load_users()
    categories = load_user_categories(user['username'])

    form = TaskForm()
    form.category.choices = [(category.id, category.name) for category in categories]
    
    if form.validate_on_submit():
        id = generate_id()

        new_task = Task(
                id,
                form.title.data,
                form.description.data,
                form.priority.data,
                form.category.data,
                created_by=user['username'],
                completed=False,
                progress=0,
                created_date=None
            )
        tasks = load_tasks()
        tasks.append(new_task)
        save_tasks(tasks)
        
        previous_url = session.pop('previous_url', url_for('index'))
        return redirect(previous_url)
    
    users = load_users()
    session['previous_url'] = request.referrer
    return render_template('add_task.html', form=form, users=users, is_logged_in=is_logged_in(), current_user=current_user())

def delete_task_route(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    
    tasks = load_user_tasks()
    
    tasks = load_tasks()

    task = next((task for task in tasks if int(task.id) == int(index)), None)

    category_filter = task.category

    tasks = [task for task in tasks if int(task.id) != int(index)]
    
    save_tasks(tasks)

    new_url = f"/?category={category_filter}"
    
    return redirect(new_url)

def edit_task_route(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    tasks = load_tasks()

    category_filter = request.args.get('category')

    if category_filter:
        tasks = [task for task in tasks if task.category == category_filter]
    else:
        tasks = []

    task = next((task for task in tasks if int(task.id) == int(index)), None)
    
    users = load_users()

    form = TaskForm(obj=task)

    form.category.choices = [(category.id, category.name) for category in load_user_categories(user['username'])]
    
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.priority = form.priority.data
        task.category = form.category.data

        save_tasks(tasks)
        
        previous_url = session.pop('previous_url', url_for('index'))
        return redirect(previous_url)
    
    session['previous_url'] = request.referrer
    return render_template('edit_task.html', users=users, form=form, is_logged_in=is_logged_in(), current_user=current_user())

def update_progress_route(task_id):
    progress = request.args.get('progress')
    tasks = load_tasks()
    task = next((task for task in tasks if int(task.id) == int(task_id)), None)

    if task:
        task.progress = progress
        save_tasks(tasks)
    
    return redirect(request.referrer)

def complete_task_route(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    
    tasks = load_user_tasks()
    
    task = next((task for task in tasks if int(task.id) == int(index)), None)

    task.completed = True

    save_tasks(tasks)
    flash("Task completed successfully.")
    return redirect(request.referrer)

def not_complete_task_route(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    
    tasks = load_user_tasks()

    task = next((task for task in tasks if int(task.id) == int(index)), None)

    task.completed = False

    save_tasks(tasks)
    return redirect(request.referrer)