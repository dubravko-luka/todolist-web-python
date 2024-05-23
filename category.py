import csv
from models import Category
from flask import render_template, request, redirect, url_for
from auth import is_logged_in, current_user
from utils import generate_slug

def load_categories():
    categories = []
    with open('database/categories.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            categories.append(Category(row[0], row[1], row[2]))
    return categories

def load_user_categories(username):
    categories = load_categories()
    return [category for category in categories if category.created_by == username]

def save_category(category_name, created_by):
    categories = load_user_categories(created_by)
    slug = generate_slug(category_name)
    if any(category.id == slug and category.created_by == created_by for category in categories):
        return False
    with open('database/categories.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([slug, category_name, created_by])
    return True
    

def add_category_route():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    if request.method == 'POST':
        category_name = request.form['category_name']
        if save_category(category_name, user['username']):
            return redirect(url_for('index'))
        else:
            error = 'Category already exists.'
            return render_template('add_category.html', error=error, is_logged_in=is_logged_in(), current_user=current_user())
    
    return render_template('add_category.html', is_logged_in=is_logged_in(), current_user=current_user())
