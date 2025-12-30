try:
    from flask import Flask, request, redirect, render_template, url_for
    from flask_sqlalchemy import SQLAlchemy
except ModuleNotFoundError:
    print("Flask or Flask_SQLAlchemy not installed. Run: pip install flask flask_sqlalchemy")
    exit()

import string
import random
from datetime import datetime
import os

app = Flask(__name__)

# Database config: SQLite stored in current folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'urls.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# URL Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_id = db.Column(db.String(10), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create database tables
with app.app_context():
    db.create_all()

# Generate random short ID
def generate_short_id(num_chars=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choice(characters) for _ in range(num_chars))
        if not URL.query.filter_by(short_id=short_id).first():
            return short_id

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['original_url']
        custom_slug = request.form.get('custom_slug')

        if not original_url.startswith(('http://', 'https://')):
            original_url = 'http://' + original_url

        if custom_slug:
            if URL.query.filter_by(short_id=custom_slug).first():
                return render_template('index.html', error="Custom slug already exists!")
            short_id = custom_slug
        else:
            short_id = generate_short_id()

        new_url = URL(original_url=original_url, short_id=short_id)
        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_id
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

# Redirect short URL
@app.route('/<short_id>')
def redirect_url(short_id):
    url = URL.query.filter_by(short_id=short_id).first()
    if url:
        url.clicks += 1
        db.session.commit()
        return redirect(url.original_url)
    return f"<h1>URL not found for ID: {short_id}</h1>", 404

# Analytics page
@app.route('/analytics')
def analytics():
    urls = URL.query.order_by(URL.created_at.desc()).all()
    return render_template('analytics.html', urls=urls)

if __name__ == "__main__":
    app.run(debug=True)
