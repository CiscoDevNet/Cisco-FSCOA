#!/usr/bin/env python
import json, re, sys, os, json, requests
import subprocess
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict

lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

import lab_vars
from lab_vars import *

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('SSH_TOKEN')


#vedge
vedge_1_index_0_pub_ip = os.getenv('vedge_1_index_0_pub_ip')
vedge_1_index_1_pub_ip = os.getenv('vedge_1_index_1_pub_ip')


url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vedge_1_index_0_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vedge_1_index_0_pub_ip": vedge_1_index_0_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vedge_1_index_1_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vedge_1_index_1_pub_ip": vedge_1_index_1_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)