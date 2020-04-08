from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS
from models import db
from myqueue import Queue


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)
Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/new', methods=['POST'])
def new_element():
    pass

@app.route('/next')
def next_element():
    pass

@app.route('/all')
def all_element():
    pass

if __name__ == '__main__':
    manager.run()