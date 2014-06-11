#!/usr/bin/env python


import sys, time, ipaddr, os, shutil
from functools import  partial
from subprocess import call, check_output
scall = partial(call, shell=True)
scheck = partial(check_output, shell=True)



def add_client(rule,ip):
  version = str(ipaddr.IPAddress(ip).version)
  if version == '4': command = "/sbin/iptables -t filter -A FORWARD %s %s -j ACCEPT" %(rule, ip)
  else: command = "/sbin/ip6tables -t filter -A FORWARD %s %s -j ACCEPT" %(rule,ip)
  scall(command)


add_client('-s','10.0.0.1')
add_client('-d','10.0.0.1')
add_client('-s','fe33::1')
add_client('-d','fe33::1')
