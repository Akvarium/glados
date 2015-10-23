#!/usr/bin/python
import pam,sys

pam = pam.pam()







def clogin(user,pw):
    #pw = pw.decode('base64')
    return pam.authenticate(user,pw)


print clogin(sys.argv[1],sys.argv[2])

