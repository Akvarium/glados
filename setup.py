#!/usr/bin/env python

from distutils.core import setup

setup(name='glados',
    version='0.3.4',
    description='captivePortalThingy',
    author='Svein Ove Undal',
    author_email='sveinov@uninett.no',
    url='http://tihlde.org/sveinou/glados.git',
    py_modules = ['wall','tower'],
    scripts=['bin/lan','bin/startlan','bin/startlan6','bin/flushlan'],
    data_files=[('/etc/dhcp/', ['dhcpd.conf']),
	       ('/etc/',['glados.conf']),
	       ('/var/log/',['tower.log']),
	       ('/var/www/html/',['html/1336.png','html/IzUaG.gif','html/ipfire.png','html/worldTux.png','html/index.php','html/pam.py','auth.py']),]
    )
