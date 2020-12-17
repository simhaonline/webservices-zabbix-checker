#!/usr/bin/python3
import requests
import sys

web_service_url = sys.argv[1]
web_service_code = sys.argv[2]

try:
    web_service_base_login = sys.argv[3]
    web_service_base_password = sys.argv[4]
    web_service_skip_base_auth = False
except:
    web_service_skip_base_auth = True

try:
    if web_service_skip_base_auth:
        r = requests.get(web_service_url, allow_redirects=False)
    else:
        r = requests.get(web_service_url, allow_redirects=False, auth=(web_service_base_login, web_service_base_password))
    status_code = r.status_code
except:
    status_code = 0

if int(status_code) == int(web_service_code):
    print (1)
else: 
    print (0)