from fib import fib

from socket import *
from threading import Thread

def fib_server(address):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sock.bind(address)
	sock.listen(5)  #queue up to 5 connect requests
	while True:
		clientsock, addr = sock.accept()  #blocking
		print "Connection", addr
		t = Thread(target=fib_handler, args=(clientsock,))
		#daemon thread = we don't need to tell it to exit when this python program finishes
		t.daemon=True 
		t.start()

def fib_handler(clientsock):
	while True:
		req = clientsock.recv(100)
		if not req: 
			break
		n = int(req)  #requests are strings. this will break if int() doesn't work
		result = fib(n)
		resp = str(result).encode('ascii') + b'\n'  #b for bytes
		clientsock.send(resp)
	print "Closed"

#localhost port 25000
fib_server(('', 25000))