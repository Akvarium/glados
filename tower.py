import socket, ipaddr, hashlib, json
from wall import wall
from time import strftime
adminHash = hashlib.sha224("nijet").hexdigest()
pam = PAM.pam()

class tower():

  def __init__(self,port):
    self.sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    self.sock.bind(('',port))
    self.logfile = open('log', 'w')
  

  def listen(self):
    running = True 
    while running:
      data, addr = self.sock.recvfrom(1024)
      if self.is_accepted(addr, data):
        self.command(addr, data.replace('\n',''))
      else: self.log(addr, data.replace('\n',''), 'No Acces!')
       
  def is_accepted(self,stuffs, data):
    return True 

  def log(self,addr,data,code):
    out = {'ip': addr[0],'data': data,'code': code, 'when': strftime("%d %b %Y %H:%M:%S")}
    print out 
    json.dump(out, self.logfile)


  def command(self,addr,data):
    if len(data.split()) == 3 and wall.get_IPv(data.split()[2]) > 0:
      if 'add' in data: 
        wall.add_client(data.split()[2])
        self.log(addr,data,'Add')
      if 'del' in data:
        wall.del_client(data.split()[2])
	self.log(addr,data,'del')

    if 'rules' in data:
      self.log(addr,wall.get_rules(int(data.split()[1])),'rules')

  def __del__():
    self.logfile.close()
      


tower = tower(5000)

tower.listen()
