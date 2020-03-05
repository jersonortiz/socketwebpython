import sys
import client_socket
from os import environ
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

host = "127.0.0.1"
port = 8090
client = client_socket.client_socket();


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login',methods=['get','POST'])
def Login():
	values = request.get_json()
	print(str(values))

	client.connect(host, port)


@socketio.on('message')
def test_message(message):
	print(message)
	print("movimiento")
	emit('most', {'data': message['nombre']})


@socketio.on('connect')
def test_connect():
	print("conectado")
	emit('message', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
	print('Client disconnected')

if __name__ == '__main__':
	socketio.run(app)