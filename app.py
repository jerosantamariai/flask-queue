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

_queue = Queue()

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/new', methods=['POST'])
def new_element():
    
    name = request.json.get('name', None)
    phone = request.json.get('phone', None)

    if not name or name == '':
        return jsonify({"msg": "Debes ingresar tu nombre"}), 400
    if not phone or phone == '':
        return jsonify({"msg": "Debes ingresar tu telefono"}), 400

    item = {
        "name": name,
        "phone": phone
    }
    
    result = _queue.enqueue(item)
    return jsonify({"msj": "Hola! Entraste en la lista!"}), 200

@app.route('/next', methods=['GET'])
def next_element():
    result = _queue.dequeue()
    return jsonify({"msj": "Cliente ha salido de la lista"}), 200

@app.route('/all')
def all_element():
    users = _queue.get_queue()
    return jsonify(users), 200

if __name__ == '__main__':
    manager.run()