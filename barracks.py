#!/usr/bin/env python2.7

class Barraks():




  def file_w(self,line,file_path):
    f = open(path, 'a+r')
    f.write(line+'\n'\)
    f.close()

  def is_in_file(self,word,file_path):
    out = False
    f = open(path, 'r')
    if word in f.read(): out True
    f.close()
    return out

  def file_mod(self,txt,path,search,replace=False):
    if txt in open(path, 'r').read(): return
    isline = False
    for line in fileinput.input(path, inplace=1):
      if search in line: isline = True
      else:
        if isline: print txt
        isline = False
        if replace: break
      print line,

  def find_if(self):
    """ uses ifconfig to find your network-interfaces """
    ifconfig = check_output("/sbin/ifconfig -a", shell=True).split()
    prev_word = ifconfig[0]
    interfaces = ""
    for word in ifconfig:
      if word == "Link" and prev_word != "lo" and prev_word != "Link":
        interfaces += " " + prev_word
      prev_word = word
    return interfaces.strip()

  def add_interface(self,IF,address,gateway=False):
    #if IF in file, replace
    #else write
    if is_in_file(IF):
      #remove line IF

