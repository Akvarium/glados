### words with meaning




## Dependencies

python-ipaddr
python-dnspython
python-configparser

apache2 with php-plugin

isc-dhcp-server

shit uses PAM to authenticate, needs libpam-ldap(d) to work with ldap(d). 


## INSTALLATION


 python setup.py --install

## configure

change the /etc/dhcp/dhcpd.conf to use your network

change the /etc/glados.conf do suit your needs

change the /var/www/html/index.php $ADMIP to the lan side IP, remember the $ADMPORT


## ussage

start the lan thingy with the command, (remember the $ADMPORT?)

 lan --start <port>


This starts the tower.py file, witch throws up a simple datagram listen soccet. This soccet takes some basic commands like

nc -u 127.0.0.1 $port add $user $ip
or
nc -u 127.0.0.1 $port del $ip

witch then usess the wall.py to change the iptalbes rules of the machine.


