# Flask Cliff Notes - Python Web Framework

## Installation & Quick Start

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows: 
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install Flask
pip install flask

# Create app
touch app.py
```

## Minimal Flask App

```python name=app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for

# CREATE APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'

# ROUTE:  Homepage
@app.route('/')
def home():
    return "Hello, Flask!"

# ROUTE: With HTML template
@app.route('/hello')
def hello():
    name = "Floyd"
    return render_template('hello.html', name=name)

# ROUTE: With URL parameter
@app.route('/user/<username>')
def user_profile(username):
    return f"Profile page for {username}"

# ROUTE: Query parameters (?name=Floyd)
@app.route('/greet')
def greet():
    name = request.args.get('name', 'World')
    return f"Hello, {name}!"

# ROUTE: POST request (forms)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Received: {name}, {email}"
    return render_template('form.html')

# ROUTE: JSON API
@app.route('/api/data')
def api_data():
    data = {
        'status': 'success',
        'items': [1, 2, 3, 4, 5]
    }
    return jsonify(data)

# ROUTE:  Redirect
@app.route('/old-page')
def old_page():
    return redirect(url_for('home'))

# ERROR HANDLER:  404
@app.errorhandler(404)
def not_found(error):
    return "Page not found!", 404

# RUN APP
if __name__ == '__main__':
    app. run(debug=True)  # debug=True for development only! 
```

## Flask Project Structure

```
my-flask-app/
├── venv/                  # Virtual environment
├── app. py                 # Main application
├── requirements.txt       # Dependencies
├── static/                # CSS, JS, images
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
└── templates/             # HTML files
    ├── base.html
    ├── index.html
    └── form.html
```

## HTML Templates (Jinja2)

```html name=templates/base.html
<! DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Flask App{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('home') }}">Home</a>
        <a href="{{ url_for('about') }}">About</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2026 My Flask App</p>
    </footer>

    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```

```html name=templates/index.html
{% extends 'base.html' %}

{% block title %}Home - My Flask App{% endblock %}

{% block content %}
<h1>Welcome, {{ name }}!</h1>

<!-- IF statement -->
{% if user_logged_in %}
    <p>Welcome back! </p>
{% else %}
    <p>Please log in. </p>
{% endif %}

<!-- FOR loop -->
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

<!-- Form -->
<form method="POST" action="{{ url_for('submit') }}">
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <button type="submit">Submit</button>
</form>
{% endblock %}
```

## Flask with Database (SQLite)

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# DEFINE MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self. name}>'

# CREATE TABLES
with app.app_context():
    db.create_all()

# CREATE new user
@app.route('/add-user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    
    return "User added!"

# READ all users
@app.route('/users')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)

# READ one user
@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user.html', user=user)

# UPDATE user
@app.route('/update-user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    user.name = request.form['name']
    user.email = request.form['email']
    db.session.commit()
    return "User updated!"

# DELETE user
@app.route('/delete-user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return "User deleted!"
```

## Flask API Template

```python name=api.py
from flask import Flask, jsonify, request
from flask_cors import CORS  # pip install flask-cors

app = Flask(__name__)
CORS(app)  # Allow requests from React/other frontends

# Sample data (in real app, use database)
items = [
    {'id': 1, 'name': 'Item 1', 'description':  'First item'},
    {'id': 2, 'name': 'Item 2', 'description':  'Second item'}
]

# GET all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET single item
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# POST new item
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    
    new_item = {
        'id': len(items) + 1,
        'name': data. get('name'),
        'description': data.get('description')
    }
    items.append(new_item)
    
    return jsonify(new_item), 201

# PUT update item
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    data = request.get_json()
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    
    return jsonify(item)

# DELETE item
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [i for i in items if i['id'] != item_id]
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__': 
    app.run(debug=True, port=5000)
```

## Common Flask Patterns

```python
# FILE UPLOADS
from werkzeug.utils import secure_filename
import os

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file", 400
    
    file = request.files['file']
    if file.filename == '': 
        return "No file selected", 400
    
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return "File uploaded!"

# SESSIONS
from flask import session

@app.route('/login', methods=['POST'])
def login():
    session['user_id'] = 123
    session['username'] = 'floyd'
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# COOKIES
from flask import make_response

@app.route('/set-cookie')
def set_cookie():
    resp = make_response("Cookie set!")
    resp.set_cookie('username', 'floyd')
    return resp

@app.route('/get-cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f"Username: {username}"

# FLASH MESSAGES
from flask import flash

@app.route('/action')
def action():
    flash('Success!', 'success')
    flash('Warning!', 'warning')
    flash('Error!', 'error')
    return redirect(url_for('home'))

# In template:
# {% with messages = get_flashed_messages(with_categories=true) %}
#   {% for category, message in messages %}
#     <div class="alert alert-{{ category }}">{{ message }}</div>
#   {% endfor %}
# {% endwith %}
```

## Quick Reference

| Task | Code |
|------|------|
| Create route | `@app.route('/path')` |
| Get form data | `request.form['key']` |
| Get query param | `request.args.get('key')` |
| Get JSON | `request.get_json()` |
| Return JSON | `jsonify(data)` |
| Render template | `render_template('file.html', var=value)` |
| Redirect | `redirect(url_for('function_name'))` |
| Set session | `session['key'] = value` |
| Flash message | `flash('message', 'category')` |

## Run Flask App

```bash
# Development
python app.py

# Or with flask command
export FLASK_APP=app.py  # Linux/Mac
set FLASK_APP=app.py     # Windows

flask run

# With auto-reload
flask run --debug

# On different port
flask run --port=8000

# Accessible from network
flask run --host=0.0.0.0
```

---
**Notes Section**:
- Routes = URLs your app responds to
- render_template = show HTML
- jsonify = return JSON (for APIs)
- request. form = form data
- request.args = URL parameters
- 
```