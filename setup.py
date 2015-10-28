#!/usr/bin/env python

from distutils.core import setup

setup(name='glados',
    version='0.3.4',
    description='captivePortalThingy',
    author='Svein Ove Undal',
    author_email='sveinov@uninett.no',
    url='http://tihlde.org/sveinou/glados.git',
    py_modules = ['wall','tower'],
    scripts=['bin/*'],
    data_files=[('/etc/dhcp/', ['dhcpd.conf']),
               [('/var/www/html/'['html/*']),
)
