
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route('/')
def home():
       projects = [
           {"title": "Projet 1", "description": "Une application web innovante.", "link": "#"},
           {"title": "Projet 2", "description": "Système de gestion de données.", "link": "#"},
           {"title": "Projet 3", "description": "Portfolio interactif.", "link": "#"}
       ]
       return render_template('index.html', projects=projects)

@app.route('/contact', methods=['POST'])
def contact():
       name = request.form.get('name')
       email = request.form.get('email')
       message = request.form.get('message')
       print(f"Message reçu de {name} ({email}): {message}")
       return redirect(url_for('home'))

if __name__ == '__main__':
       app.run()