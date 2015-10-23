#!/usr/bin/env python

import sys, time, ipaddr, os, shutil
from functools import  partial
from subprocess import call, check_output
scall = partial(call, shell=True)
scheck = partial(check_output, shell=True)

class wall():



  def add_client(self,ip,user):
    ver = self.get_IPv(ip)
    self.del_client(ip)
    for way in ['-d','-s']:
      command = '-A ALLOWED %s %s -j ACCEPT -m comment --comment %s' %(way,ip,user)
      if ver == 4: 
        scall('/sbin/iptables %s' %command)
        scall('/sbin/iptables -t nat %s' %command)
      elif ver == 6: 
        scall('/sbin/ip6tables %s'%command)
        scall('/sbin/ip6tables -t nat %s'%command)
      scall("iptables-save > /var/www/html/active")

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
        if ver == 4: 
          scall('/sbin/iptables %s' %command)
          scall('/sbin/iptables -t nat %s' %command)
        elif ver == 6: 
          scall('/sbin/ip6tables %s'%command)
          scall('/sbin/ip6tables -t nat %s'%command)

        scall("iptables-save > /var/www/html/active")
      

  def get_rules(self,ver):	
    out = ''
    rules = '' 
    if ver == 4: rules = scheck("/sbin/iptables-save")
    elif ver == 6: rules = scheck("/sbin/ip6tables-save")
    rules = rules.split('*filter')[1]
    for rules in rules.split('\n'):
      if 'ALLOWED' in rules and not '[0:0]' in rules: out += rules+"; "
 
    out = out.split(';')
    out = out[:len(out)-1]

    return out 

  def get_ns(self,data):
    ver = self.get_IPv(data)
    out = ''
    try:
      if ver > 0: return scheck('host %s' %data).split()[-1]  
      elif ver == -1:
        for line in scheck('host %s' %data).split('\n'):
	  if line and not 'mail' in line: out += line.split()[-1]+' ' 
    except Exception, e: print e 
    return out.split()

  def add_client_from_ns(self,address):
    for ip in self.get_ns(address):
      self.add_client(ip)




wall = wall()
