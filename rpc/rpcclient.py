import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9090')
print proxy.sum(4,5)
