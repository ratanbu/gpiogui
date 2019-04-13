#! /usr/bin/python3
import socket
from threading import  *


class network(Thread):
    def __init__(self, hostid,portno,maxbytesize):
        Thread.__init__(self)
        #create a socket object
        self.s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #get local machine name
        self.host = socket.gethostname()
        self.host=hostid
        self.port = portno
        self.bytesize = maxbytesize
        self.start()

    def connectoport(self):
    #def run(self):
        addr= (self.host, int(self.port))
        try:
            self.s.connect(addr)
        except socket.error:
            print ("unable to connect to ip %s" %(self.host))
            return False
        else:
            print("Connected to ip %s" %(self.host))
            return True

    def senddata(self,data):
        print("%s" %(data))
        self.s.sendall(data.encode())

    def receive(self):
        msg = self.s.recv(self.bytesize)
        return msg

    def closeconnection(self):
        self.s.close()

    def networkerror(self):
        return self.s.error

    def convertIpToInt(self,ip):
        return sum([int(ipField) << 8*index for index, ipField in enumerate(reversed(ip.split('.')))])
