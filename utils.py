
import random
import string

def generate_slug(name):
    return name.lower().replace(' ', '-')

def generate_id():
    return ''.join(random.choices('0123456789', k=10))
