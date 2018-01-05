#! python3

try:
	# Python 2.x
	from SocketServer import ThreadingMixIn
	from SimpleHTTPServer import SimpleHTTPRequestHandler
	from BaseHTTPServer import HTTPServer
except ImportError:
	# Python 3.x
	from socketserver import ThreadingMixIn
	from http.server import SimpleHTTPRequestHandler, HTTPServer

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
	pass

import sys
import os

port = ''

if sys.argv[1:]:
	port = sys.argv[1]
	
if not port.isdigit():
	while True:
		try:
			port = int(input("Enter port (default = 80): "))
		except ValueError:
			print("INVALID PORT")
			continue
		else:
			break

port = int(port)
directory = ''
if sys.argv[2:]:
	directory = sys.argv[2]
	
if not os.path.isdir(directory):
	directory = input("Enter directory to start server: ")

while not os.path.isdir(directory):
		print("INVALID DIRECTORY!")
		directory = input("Enter directory to start server: ")

os.chdir(directory)
directory = os.getcwd()

os.system('cls||clear')
	
print ('Server started on port %s at %s' % (port, directory))
print ('Close Command Window to end.')

server = ThreadingSimpleServer(('', port), SimpleHTTPRequestHandler)

try:
	while 1:
		sys.stdout.flush()
		server.handle_request()
except KeyboardInterrupt:
	print("Finished")