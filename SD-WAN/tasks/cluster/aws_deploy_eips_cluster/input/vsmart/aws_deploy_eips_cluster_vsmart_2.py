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

#create 3 eips for vsmart_2 and tag

#vsmart_2_index0
cmd='aws ec2 allocate-address --region' + " " + "{}".format(region) + " " + '--tag-specifications' + " " + "'ResourceType=elastic-ip,Tags=[{Key=Name,Value=vsmart_2_index_0}]'"
output = check_output("{}".format(cmd), shell=True).decode().strip()
#print("Output: \n{}\n".format(output))
result = json.loads(output)
vsmart_2_index_0_AllocationId = (result['AllocationId'])
print(vsmart_2_index_0_AllocationId)
#write the eip to the vault so it can be associated with the correct NICs once the instances come up
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vsmart_2_index_0_AllocationId"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
#data = f'{{"token": "{TOKEN}"}}'
data_json = {"vsmart_2_index_0_AllocationId": vsmart_2_index_0_AllocationId }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#vsmart_2_index1
cmd='aws ec2 allocate-address --region' + " " + "{}".format(region) + " " + '--tag-specifications' + " " + "'ResourceType=elastic-ip,Tags=[{Key=Name,Value=vsmart_2_index_1}]'"
output = check_output("{}".format(cmd), shell=True).decode().strip()
#print("Output: \n{}\n".format(output))
result = json.loads(output)
vsmart_2_index_1_AllocationId = (result['AllocationId'])
print(vsmart_2_index_1_AllocationId)
#write the eip to the vault so it can be associated with the correct NICs once the instances come up
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vsmart_2_index_1_AllocationId"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
#data = f'{{"token": "{TOKEN}"}}'
data_json = {"vsmart_2_index_1_AllocationId": vsmart_2_index_1_AllocationId }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)







