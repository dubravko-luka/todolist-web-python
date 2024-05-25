import csv
from models import Category
from flask import render_template, request, redirect, url_for
from auth import is_logged_in, current_user, load_users
from utils import generate_slug

def load_categories():
    categories = []
    with open('database/categories.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            categories.append(Category(row[0], row[1], row[2]))
    return categories

def is_slug_exists(categories, new_slug):
    for category in categories:
        if category.id == new_slug:
            return True
    return False

def load_user_categories(username):
    categories = load_categories()
    return [category for category in categories if category.created_by == username]

def save_category(category_name, created_by):
    categories = load_user_categories(created_by)

    slug_new = generate_slug(category_name)

    slug_index = 0

    slug = slug_new
    while is_slug_exists(categories, slug):
        slug = slug_new + '-' + str(slug_index)
        slug_index += 1

    with open('database/categories.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([slug, category_name, created_by])
    return True

def save_categories(categories):
    with open('database/categories.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for category in categories:
            writer.writerow([category.id, category.name, category.created_by])

def add_category_route():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    if request.method == 'POST':
        category_name = request.form['category_name']
        if save_category(category_name, user['username']):
            return render_template('add_category.html', is_logged_in=is_logged_in(), current_user=current_user())
        else:
            error = 'Category already exists.'
            return render_template('add_category.html', error=error, is_logged_in=is_logged_in(), current_user=current_user())
    
    return render_template('add_category.html', is_logged_in=is_logged_in(), current_user=current_user())

def categories_route():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    user = current_user()
    categories = load_user_categories(user['username'])
    # Update
    if request.method == 'POST':
        category_id = request.form.get('category_id')
        new_name = request.form.get('new_name')

        categoriesAll = load_categories()

        category = next((category for category in categoriesAll if category.id == category_id), None)
        
        category.name = new_name
        save_categories(categoriesAll)

        return redirect(url_for('categories'))
    
    return render_template('categories.html', categories=categories, is_logged_in=is_logged_in(), current_user=current_user())


def delete_category_route(index):
    if not is_logged_in():
        return redirect(url_for('login'))
    
    categories = load_categories()

    categories = [category for category in categories if category.id != index]
    
    save_categories(categories)
    
    return redirect(request.referrer)