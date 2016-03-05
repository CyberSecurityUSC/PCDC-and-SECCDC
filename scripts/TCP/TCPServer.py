#TCP server from "Black Hat Python"
import socket
import threading

#replace with desired ip address and port
bind_ip = "0.0.0.0"
bind_port = 9999

#start listening
server.bind(bind_ip, bind_port)

#maximum of 5 connections
server.listen(5)


print "[*] Listening on %s:%d" % (bind_ip,bind_port)

def handle_client(client_socket):

	request = client_socket.recv(1024)

	print "[*] Recieved: %s" %request

	client_socket.send("ACK!")

	client_socket.close()

while True:

	client,addr = server.accept()

	print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()

