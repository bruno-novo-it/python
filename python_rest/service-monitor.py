#! /usr/bin/env python

##############
#
# Script to verify if a api is up and running
#
# Get from: https://motoma.io/basic-server-monitoring-with-python/
#
# Other related sites:
#
# https://www.eriwen.com/python/site-monitor/
#
# https://github.com/damyanbogoev/flask-bookshelf
#
# http://linuxsay.com/t/python-linux-monitoring-tool/490
#
####################

from urllib.request import urlopen
from socket import socket
from sys import argv

def tcp_test(server_info):
    cpos = server_info.find(':')
    try:
        sock = socket()
        sock.connect((server_info[:cpos], int(server_info[cpos+1:])))
        sock.close
        return True
    except:
        return False

def http_test(server_info):
    try:
        data = urlopen(server_info)
        print(server_info, '\t\tStatus --> %d' % data.code)
        return True
    except:
        return False

def server_test(test_type, server_info):
    if test_type.lower() == 'tcp':
        return tcp_test(server_info)
    elif test_type.lower() == 'http':
        return http_test(server_info)

if __name__ == '__main__':
    if len(argv) != 3:
        print('Wrong number of arguments.')
    elif not server_test(argv[1], argv[2]):
    	 print('Unable to connect to the service %s %s.' % (argv[1].upper(), argv[2]))
