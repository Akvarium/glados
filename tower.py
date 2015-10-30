#!/usr/bin/python
import socket, ipaddr, hashlib, json, time, dns.query, dns.update
from wall import wall
from ConfigParser import SafeConfigParser
adminHash = hashlib.sha224("nijet").hexdigest()

class tower():

  def __init__(self,port):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock.bind(('',port))
    parser = SafeConfigParser()
    parser.read('/etc/glados.conf')
    self.wall = wall(parser.read('global','ipv6_prefix'))
    self.logfile = open(parser.get('global','logfile'))
    self.allowed = parser.get('global','allowed_net')
    self.zone = parser.get('global','dns_zone')
    self.dns_server = parser.get('global','dns_server')

  def listen(self):
    running = True
    while running:
      data, addr = self.sock.recvfrom(1024)
      if self.is_accepted(addr, data):
        self.command(addr, data.replace('\n',''))
      else: self.log(addr, data.replace('\n',''), 'No Acces!')

  def is_accepted(self,addr, data):
    if addr[0] in self.allowed: return True
    else: return False

  def log(self,addr,data,code):
    out = {'ip': addr[0],'data': data,'code': code, 'when': time.strftime("%d %b %Y %H:%M:%S")}
    self.logfile.write(str(out)+'\n')
    print out


  def command(self,addr,data):
    if len(data.split()) == 3 and self.wall.get_IPv(data.split()[2]) > 0:
      if 'add' in data:
        self.wall.add_client(data.split()[2],data.split()[1])
        self.log(addr,data,'Add')
        self.add_dns(self.zone,data.split()[1],data.split()[2])
      if 'del' in data:
        self.del_dns(self.zone,data.split()[1],data.split()[2])
	self.log(addr,data,'del')
        self.wall.del_client(data.split()[2])

    if 'rules' in data:
      self.log(addr,self.wall.get_rules(int(data.split()[1])),'rules')

  def add_dns(self,zone,user,ip):
    ver = self.wall.get_IPv(ip)
    update = dns.update.Update(zone)
    code = 'A'
    if ver == 6: return "noIpv6"
    update.replace(user,15,code,ip)
    return dns.query.tcp(update, self.dns_server)

  def del_dns(self,zone,host,IP):
     try:
       if host == 'dhcp': host = self.get_user(IP)
     except Exception, e: print e
     print host
     update = dns.update.Update(zone)
     update.delete(host)
     return dns.query.tcp(update, self.dns_server)

  def get_user(self,IP):
    ipt = self.wall.get_rules(4)
    print ipt
    for x in ipt:
      print x
      if IP in x: return x.split()[7]
    return "DeletedSomthingThatWasRemowed??"


