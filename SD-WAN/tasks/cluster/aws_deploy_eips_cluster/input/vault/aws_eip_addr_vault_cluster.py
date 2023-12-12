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

#vmanage_1
vmanage_1_index_0_pub_ip = os.getenv('vmanage_1_index_0_pub_ip')
vmanage_1_index_1_pub_ip = os.getenv('vmanage_1_index_1_pub_ip')
vmanage_1_index_2_pub_ip = os.getenv('vmanage_1_index_2_pub_ip')
#vmanage_2
vmanage_2_index_0_pub_ip = os.getenv('vmanage_2_index_0_pub_ip')
vmanage_2_index_1_pub_ip = os.getenv('vmanage_2_index_1_pub_ip')
vmanage_2_index_2_pub_ip = os.getenv('vmanage_2_index_2_pub_ip')
#vmanage_3
vmanage_3_index_0_pub_ip = os.getenv('vmanage_3_index_0_pub_ip')
vmanage_3_index_1_pub_ip = os.getenv('vmanage_3_index_1_pub_ip')
vmanage_3_index_2_pub_ip = os.getenv('vmanage_3_index_2_pub_ip')

#vbond_1
vbond_1_index_0_pub_ip = os.getenv('vbond_1_index_0_pub_ip')
vbond_1_index_1_pub_ip = os.getenv('vbond_1_index_1_pub_ip')
#vbond_2
vbond_2_index_0_pub_ip = os.getenv('vbond_2_index_0_pub_ip')
vbond_2_index_1_pub_ip = os.getenv('vbond_2_index_1_pub_ip')

#vsmart_1
vsmart_1_index_0_pub_ip = os.getenv('vsmart_1_index_0_pub_ip')
vsmart_1_index_1_pub_ip = os.getenv('vsmart_1_index_1_pub_ip')
#vsmart_2
vsmart_2_index_0_pub_ip = os.getenv('vsmart_2_index_0_pub_ip')
vsmart_2_index_1_pub_ip = os.getenv('vsmart_2_index_1_pub_ip')

#vedge
vedge_1_index_0_pub_ip = os.getenv('vedge_1_index_0_pub_ip')
vedge_1_index_1_pub_ip = os.getenv('vedge_1_index_1_pub_ip')

#vmanage_1
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_1_index_0_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vmanage_1_index_0_pub_ip": vmanage_1_index_0_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_1_index_1_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vmanage_1_index_1_pub_ip": vmanage_1_index_1_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_1_index_2_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vmanage_1_index_2_pub_ip": vmanage_1_index_2_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#vmanage_2
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_2_index_0_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vmanage_2_index_0_pub_ip": vmanage_2_index_0_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_2_index_1_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vmanage_2_index_1_pub_ip": vmanage_2_index_1_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_2_index_2_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vmanage_2_index_2_pub_ip": vmanage_2_index_2_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#vmanage_3
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_3_index_0_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vmanage_3_index_0_pub_ip": vmanage_3_index_0_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_3_index_1_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vmanage_3_index_1_pub_ip": vmanage_3_index_1_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_3_index_2_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vmanage_3_index_2_pub_ip": vmanage_3_index_2_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#vbond_1
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vbond_1_index_0_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vbond_1_index_0_pub_ip": vbond_1_index_0_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vbond_1_index_1_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vbond_1_index_1_pub_ip": vbond_1_index_1_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#vbond_2
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vbond_2_index_0_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vbond_2_index_0_pub_ip": vbond_2_index_0_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vbond_2_index_1_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vbond_2_index_1_pub_ip": vbond_2_index_1_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)


#vsmart_1
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vsmart_1_index_0_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vsmart_1_index_0_pub_ip": vsmart_1_index_0_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vsmart_1_index_1_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vsmart_1_index_1_pub_ip": vsmart_1_index_1_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#vsmart_2
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vsmart_2_index_0_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vsmart_2_index_0_pub_ip": vsmart_2_index_0_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vsmart_2_index_1_pub_ip"
print(url)
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {"vsmart_2_index_1_pub_ip": vsmart_2_index_1_pub_ip }
resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

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