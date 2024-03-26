from flask import Flask, jsonify, request
import json

from model.client import User, SimpleUser, LoginData, LoginSucess

app = Flask(__name__)

clients = []


@app.route('/')
def index():
    return {'client': ''}


@app.route('/<name>')
def print_name(name):
    return {'client':name}


@app.route('/client')
def get_clients():
    return jsonify(clients)


@app.route('/client', methods=['POST'])
def add_client():
    client_data = request.get_json()

    try:
        client_obj = User(**client_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    clients.append(client_obj.dict())
    return jsonify({'message': 'Usuario adicionado com sucesso!'})


@app.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()

    try:
        login_obj = LoginData(**login_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    simple_user = SimpleUser(id=1, name="Lua", status=True)

    login_success = LoginSucess(user=simple_user, access_token='xxxxxxx')

    clients.append(simple_user)
    
    return login_success.json()


if __name__ == '__main__':
    app.run(debug=True)
