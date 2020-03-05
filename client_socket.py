import socket

class client_socket:

	def __init__(self):
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

	def connect(self, address, port_number):
		while True:
			try:
				print("Conectando con el servidor ...");
				#self.client_socket.settimeout(10);
				self.client_socket.connect((address, int(port_number)));
				return True;
			except:
				print("Error de Conexion" + 
					str(address) + "::" + str(port_number));
				self.__connect_failed__();
		return False;

	def __connect_failed__(self):
		choice = input("Error de Conexion, revise nuevamente la informacion Ingresada");
		exit();

	def s_send(self, command_type, msg):
		try:
			self.client_socket.send((command_type + msg).encode());
		except:
			self.__connection_lost();

	def s_recv(self, size, expected_type):
		try:
			msg = self.client_socket.recv(size).decode();
			if(msg[0] == "Q"):
				why_quit = "";
				try:
					why_quit = self.client_socket.recv(1024).decode();
				except:
					pass;
				print(msg[1:] + why_quit);
				raise Exception;
			elif(msg[0] == "E"):
				self.s_send("e", msg[1:]);
				return self.s_recv(size, expected_type);
			elif(msg[0] != expected_type):
				self.__connection_lost();
			elif(msg[0] == "I"):
				return int(msg[1:]);
			else:
				return msg[1:];
			return msg;
		except:
			self.__connection_lost();
		return None;

	def __connection_lost(self):
		print("Error: Conexion Perdida");
		try:
			self.client_socket.send("q".encode());
		except:
			pass;
		raise Exception;

	def close(self):	
		self.client_socket.shutdown(socket.SHUT_RDWR);
		self.client_socket.close();