#!/usr/bin/python3
import requests
import sys
from datetime import datetime

operation = sys.argv[1]
web_service_url = sys.argv[2]
web_service_need_check = sys.argv[3]

if str(web_service_need_check) == '1':
    if operation == 'is_valid':
        print (1)
        sys.exit()
    if operation == 'days_left':
        print (0)
        sys.exit()
else:
    print (1)