#!/usr/bin/python3
import json

web_service_list_file = '/etc/zabbix/webservice-list.txt'
web_services = []

for line in open(web_service_list_file, 'r').read().split('\n'):
    if line == '':
        continue
    if line[0] != '#':
        tmp = line.split(';')
        web_service_url = tmp[0].strip()
        base_login = tmp[1].strip()
        base_password = tmp[2].strip()
        ssl_check = tmp[3].strip()
        normal_code = tmp[4].strip()
        web_services.append({"{#WEB_SERVICE_URL}" : web_service_url,
                            "{#BASE_LOGIN}" : base_login,
                            "{#BASE_PASSWORD}" : base_password,
                            "{#SSL_CHECK}" : ssl_check,
                            "{#NORMAL_CODE}" : normal_code})

output={"data":web_services}
print (json.dumps(output))