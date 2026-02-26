from app import app
from flask import render_template, request, redirect, url_for, flash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input', '').strip()
    if user_input:
        return redirect(f'/{user_input}')
    return redirect(url_for('home'))

@app.route('/wortel')
def wortel():
    return render_template('wortel.html')

@app.route('/<path:input>')
def dynamic_page(input):
    flash("Helaas, dit werkt niet.")
    return redirect(url_for('home'))