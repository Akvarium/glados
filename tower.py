#!/usr/bin/env python

import socket, ipaddr


class tower():

  def __init__(self,listen,port):
    try: ver = ipaddr.IPAddress(listen).version
    except Exception, e: 
      print e 
      exit(9) 

    if ver == 4: self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else: self.sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    self.sock.bind((listen, port))



  def listen(self):
    while True:
      data, addr = self.sock.recvfrom(1024)
      print data, addr




tower = tower('2001:4662:9ff8:0:1e4b:d6ff:fe88:f5f9',5000)

tower.listen()
	
    
