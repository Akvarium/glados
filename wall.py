#!/usr/bin/env python


import sys, time, ipaddr, os, shutil
from functools import  partial
from subprocess import call, check_output
scall = partial(call, shell=True)
scheck = partial(check_output, shell=True)

class wall():



  def add_client(self,ip):
    ver = self.get_IPv(ip)
    self.del_client(ip)
    for way in ['-d','-s']:
      command = '-A FORWARD %s %s -j ACCEPT' %(way,ip)
      if ver == 4: scall('/sbin/iptables %s' %command)
      elif ver == 6: scall('/sbin/ip6tables %s'%command)

  def add_custom(self,rule):
    for word in rule.split():
      ver = self.get_IPv(word)
      if ver == 4: 
        scall('/sbin/iptables %s' %rule)
	break
      elif ver == 6: 
        scall('/sbin/ip6tables %s' %rule)
	break

  def get_IPv(self,ip):
    try: return ipaddr.IPAddress(ip).version
    except Exception, e: return -1

  def del_client(self,ip):
    command = ''
    ver = self.get_IPv(ip)
    for rule in self.get_rules(ver):
      if ip in rule: 
        command = rule.replace('-A','-D')
	if ver == 4: scall('/sbin/iptables %s' %command)
        elif ver == 6: scall('/sbin/ip6tables %s' %command)
      

  def get_rules(self,ver):	
    out = ''
    rules = '' 
    if ver == 4: rules = scheck("/sbin/iptables-save")
    elif ver == 6: rules = scheck("/sbin/ip6tables-save")
    for rules in rules.split('\n'):
      if 'FORWARD' in rules and not '[0:0]' in rules: out += rules+"; "
 
    out = out.split(';')
    out = out[:len(out)-1]

    return out 





wall = wall()

print wall.get_rules(6)
print wall.get_rules(4) 
time.sleep(2)

wall.add_custom('-I INPUT -d fe34:1:39::1 -j DROP')

#wall.del_client('10.0.0.1')
#wall.del_client('fe33::1')
wall.add_client('10.0.0.1')
wall.add_client('fe33::1')
