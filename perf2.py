#requests/sec of fast requests

from socket import *
import time
from threading import Thread

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))

n = 0
def monitor():
	global n  #tell python to modify the n on the line above, instead of using local var n
	while True:
		time.sleep(1)
		print n, 'reqs/sec'
		n = 0
t = Thread(target=monitor)
t.daemon = True
t.start()

while True:
	sock.send(b'1')
	resp = sock.recv(100)
	n += 1