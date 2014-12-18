from SimpleXMLRPCServer import SimpleXMLRPCServer
import logging
import os

server = SimpleXMLRPCServer(('localhost', 9090), logRequests=True)

def sum(a, b):
	return a+b
server.register_function(sum)
try:
	server.serve_forever()
except KeyboardInterrupt:
	print 'exit'
