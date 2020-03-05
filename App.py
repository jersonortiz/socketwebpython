import sys
import client_socket
from os import environ
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

host = "127.0.0.1"
port = 8090
client = client_socket.client_socket();
player_id=""


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login',methods=['get','POST'])
def Login():
	global client
	values = request.get_json()
	print(str(values))




@socketio.on('message')
def message(message):
	print(message)
	print("movimiento")
	emit('most', {'data': message['nombre']})


@socketio.on('player_move')
def move(message):
	global client
	client.s_send("i", str(message['data']));
	command = update_board()

	#emit('most', {'data': message['data']})

@socketio.on('connect')
def connect():
	print("conectado")
	global player
	global client
	client.connect(host, port)

	player_id = int(client.s_recv(128, "A"))
	client.s_send("c","1")

	role = str(self.s_recv(2, "R"))
	client.s_send("c","2")

	client.match_id = int(client.s_recv(128, "I"));
	client.s_send("c","3")

	#print(("Tu estas jugando ahora con: " + str(client.match_id) 
	#+ "\nTu simbolo es :  \"" + role + "\""));

	emit('define_role', {'data': role})
	command = update_board()


	if(command == "Y"):
		emit('player_move', {'data':'move'})
	elif(command == "N"):
		emit('player_wait', {'data':'wait'})
		opponent_move_made = self.s_recv(2, "I");
		command = update_board()

	

@socketio.on('disconnect')
def test_disconnect():
	print('Client disconnected')


def actions(command):

	if(command == "Y"):
		player_move()
	elif(command == "N"):
		emit('player_wait', {'data':'wait'})
		opponent_move_made = self.s_recv(2, "I");
		command = update_board()

	elif(command == "D"):
		print("It's a draw.");
		## finaliza conexion
	elif(command == "W"):
		print("Ganaste!");
		
		## finaliza conexion
	elif(command == "L"):
		print("Perdiste.");
		
		## finaliza la conexxion
	
		


def player_move():
	emit('player_move', {'data':'move'})


def player_wait():



def update_board():
	global player
	global client
	board_content = client.s_recv(10, "B");
	command = client.s_recv(2, "C")
	board = format_board(command, board_content)
	emit('update_board', {'data':board})
	return command

def format_board(command, board_string):
	return( s[0] + "|" + s[1]  + "|" + s[2] + "|" + s[3] 
		+ "|" + s[4]  + "|" + s[5] + "|" + s[6] + "|" + s[7] 
		 + "|" + s[8])


if __name__ == '__main__':
	socketio.run(app)