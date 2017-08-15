import sys,socket

host=sys.argv[1]

port=70

filename=sys.argv[2]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

s.sendall(filename.encode('utf-8'))

while True:
	buf = s.recv(2048)
	if not len(buf):
		break
	sys.stdout.write(buf)

s.close()