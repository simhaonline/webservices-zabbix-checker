#!/usr/bin/python3
import requests
import sys
import datetime
import logging
import socket
import ssl

operation = sys.argv[1]
web_service_url = sys.argv[2]
web_service_need_check = sys.argv[3]
ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

def ssl_expires_in(hostname):
    """Gets the SSL cert from a given hostname and checks if it expires within buffer_days"""
    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,

    )
    # 3 second timeout because Lambda has runtime limitations
    conn.settimeout(3.0)
    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    expires = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
    return expires

if str(web_service_need_check) == '1':
    hostname = web_service_url.split('://')[1].split(':')[0]
    if operation == 'is_valid':
        print (1)
        sys.exit()
    if operation == 'days_left':
        try:
            print ((ssl_expires_in(hostname)-datetime.datetime.now()).days)
        except:
            print (0)
        sys.exit()
else:
    print (1)