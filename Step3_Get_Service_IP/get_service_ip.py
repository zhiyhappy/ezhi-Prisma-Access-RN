import json
import sys
import time
import os
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'header-api-key': 'yr0it2ejia__D9b52uxYTvaLIERbt8A5R4VHy9RJkVvuaY4EGtPY',
}

params = (
    ('fwType', 'gpcs_remote_network'),
    ('addrType', 'public_ip'),
)

response = requests.get('https://api.gpcloudservice.com/getAddrList/latest', headers=headers, params=params, verify=False)
output = dict()
output['output_information'] = response.content


# print response.content
print output['output_information']

sys.exit(0)
