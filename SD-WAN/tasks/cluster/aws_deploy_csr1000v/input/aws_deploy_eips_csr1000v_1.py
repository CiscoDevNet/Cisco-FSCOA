#!/usr/bin/env python
import json, re, sys, os, json, requests
import subprocess
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict

lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('SSH_TOKEN')

#create 3 eips for csr1000vand tag

#csr1000v_1_index0
cmd='aws ec2 allocate-address --region' + " " + "{}".format(region) + " " + '--tag-specifications' + " " + "'ResourceType=elastic-ip,Tags=[{Key=Name,Value=csr1000v_1_index_0}]'"
output = check_output("{}".format(cmd), shell=True).decode().strip()
#print("Output: \n{}\n".format(output))
result = json.loads(output)
csr1000v_1_index_0_AllocationId = (result['AllocationId'])
print(csr1000v_1_index_0_AllocationId)
#write the eip to the vault so it can be associated with the correct NICs once the instances come up
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "csr1000v_1_index_0_AllocationId"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
#data = f'{{"token": "{TOKEN}"}}'
data_json = {"csr1000v_1_index_0_AllocationId": csr1000v_1_index_0_AllocationId }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#csr1000v_1_index1
cmd='aws ec2 allocate-address --region' + " " + "{}".format(region) + " " + '--tag-specifications' + " " + "'ResourceType=elastic-ip,Tags=[{Key=Name,Value=csr1000v_1_index_1}]'"
output = check_output("{}".format(cmd), shell=True).decode().strip()
#print("Output: \n{}\n".format(output))
result = json.loads(output)
csr1000v_1_index_1_AllocationId = (result['AllocationId'])
print(csr1000v_1_index_1_AllocationId)
#write the eip to the vault so it can be associated with the correct NICs once the instances come up
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "csr1000v_1_index_1_AllocationId"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
#data = f'{{"token": "{TOKEN}"}}'
data_json = {"csr1000v_1_index_1_AllocationId": csr1000v_1_index_1_AllocationId }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)







