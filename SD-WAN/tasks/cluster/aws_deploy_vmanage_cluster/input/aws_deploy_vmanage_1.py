#!/usr/bin/env python
#This Script creates the vmanage_1 from AMI and the key - split out the key
import json, re, sys, os, json, subprocess, time, sys, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()

outfile_vars="vars"
lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('SSH_TOKEN')

ami_id = os.getenv('ami_id')
vpcid = os.getenv('vpcid')
subnetid_mgmt = os.getenv('subnetid_mgmt')
subnetid_public = os.getenv('subnetid_public')
subnetid_cluster = os.getenv('subnetid_cluster')


instance_type='c5.4xlarge'
outfile_deploy_vmanage_1='deploy-vmanage_1.json'
outfile_get_vpcid='outfile_get_vpcid.json'

inst_name="vmanage_1"
sg_name=name
priv_sg = os.getenv('priv_sg')
vmanage_1_index_0_AllocationId = os.getenv('vmanage_1_index_0_AllocationId')
vmanage_1_index_1_AllocationId = os.getenv('vmanage_1_index_1_AllocationId')
vmanage_1_index_2_AllocationId = os.getenv('vmanage_1_index_2_AllocationId')

outfile_get_sgid='outfile_sgid.json'
get_sgid='aws ec2 describe-security-groups --region' + " " + "{}".format(region) + " " + '--filters "Name=group-name,Values=' + "{}".format(sg_name) + '"'
output = check_output("{}".format(get_sgid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_get_sgid, 'w') as my_file:
    my_file.write(output)
with open (outfile_get_sgid) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['SecurityGroups']
    question_replies=question_access[0]
    question_data=question_replies['GroupId']
    sgid=question_data
    print("Printing out sgid.....")
    print(sgid)
    sgid_var=('sgid=' + "'" + "{}".format(sgid) + "'")
with open(outfile_vars, 'a+') as my_file:
    my_file.write(sgid_var + "\n")


cmd_deploy_vmanage='aws ec2 run-instances --region' + " " + "{}".format(region) + " " + '--image-id' + " " + "{}".format(ami_id) + " " + '--instance-type' + " " + "{}".format(instance_type) + " " + '--subnet-id' + " " + "{}".format(subnetid_public) +  " " + '--security-group-ids' + " " + "{}".format(sgid) + " " + "{}".format(priv_sg) + " " + '--placement AvailabilityZone=' + "{}".format(az) + " " + '--user-data file://vmanage_user_data'
output = check_output("{}".format(cmd_deploy_vmanage), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

with open(outfile_deploy_vmanage_1, 'w') as my_file:
   my_file.write(output)

with open (outfile_deploy_vmanage_1) as access_json:
   read_content = json.load(access_json)
   question_access_vmanage_1 = read_content['Instances']
   replies_access_vmanage_1 = question_access_vmanage_1[0]
   replies_data_vmanage_1=replies_access_vmanage_1['InstanceId']
   print(replies_data_vmanage_1)
   vmanage_1_instance_id=replies_data_vmanage_1 #add this to the vars file
   print(vmanage_1_instance_id)
   vmanage_1_instance_id_var=('vmanage_1_instance_id=' + "'" + "{}".format(vmanage_1_instance_id) + "'")
   vmanage_1_int_ip_addr=replies_access_vmanage_1['PrivateIpAddress']
   print(vmanage_1_int_ip_addr)

with open(outfile_vars, 'a+') as my_file:
   my_file.write(vmanage_1_instance_id_var + "\n")

vmanage_1_instance_id_var=('vmanage_1_instance_id=' + "'" + "{}".format(vmanage_1_instance_id) + "'")
print(vmanage_1_instance_id_var)
with open(outfile_vars, 'a') as my_file:
   my_file.write(vmanage_1_instance_id_var + "\n")

vmanage_1_tag_inst='aws ec2 create-tags --region' + " " + "{}".format(region) + " " + '--resources' + " " +  "{}".format(vmanage_1_instance_id) + " " + '--tags' + " " + "'" + 'Key="Name",Value=vmanage_1-1.0' + "'"
output = check_output("{}".format(vmanage_1_tag_inst), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

cmd_vmanage_1_pub_eni_id='aws ec2 describe-instances --instance-id' + " " + vmanage_1_instance_id + " " + '--query' + " " + 'Reservations[].Instances[].NetworkInterfaces[*].NetworkInterfaceId'
print(cmd_vmanage_1_pub_eni_id)
output = check_output("{}".format(cmd_vmanage_1_pub_eni_id), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

outfile_get_pub_eni_id='outfile_get_pub_eni_id.json'
with open(outfile_get_pub_eni_id, 'w') as my_file:
   my_file.write(output)
with open (outfile_get_pub_eni_id) as access_json:
   read_content = json.load(access_json)
   print(read_content)
   question_access = read_content[0]
   print(question_access)
   pub_eni_id=question_access[0]
   print(pub_eni_id)

cmd_check_instance='aws ec2 wait instance-running --instance-ids' + " " + vmanage_1_instance_id + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(cmd_check_instance), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

cmd_associate_eip_pub='aws ec2 associate-address --allocation-id' + " " + "{}".format(vmanage_1_index_0_AllocationId) + " " + '--network-interface-id' + " " + pub_eni_id
print(cmd_associate_eip_pub)
output = check_output("{}".format(cmd_associate_eip_pub), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
print("Associating eip with the pub nic")


outfile_add_vmanage_1_nic='add-vmanage_1-nic.json'
cmd_add_vmanage_1_nic='aws ec2 create-network-interface --region' + " " "{}".format(region) + " " + '--subnet-id' + " " + "{}".format(subnetid_mgmt) + " " + '--description "vmanage_1_nic_mgmt_sub"' + " " + '--groups' + " " + "{}".format(sgid) + " " + "{}".format(priv_sg) + " " + '--tag-specifications' + " " + "'ResourceType=network-interface,Tags=[{Key=Name,Value=" + "{}".format(name) + "index_1" + '}]'"" + "'"
output = check_output("{}".format(cmd_add_vmanage_1_nic), shell=True).decode().strip()
("Creating Secondary NIC on mgmt Subne....t")
print("Output: \n{}\n".format(output))
with open(outfile_add_vmanage_1_nic, 'w') as my_file:
   my_file.write(output)


with open(outfile_add_vmanage_1_nic) as access_json:
   read_content = json.load(access_json)
   print(read_content)
   question_access=read_content['NetworkInterface']
   question_data=question_access['NetworkInterfaceId']
   mgmt_eni_id=question_data
   mgmt_eni_id_var=('eni_id=' + "'" + "{}".format(mgmt_eni_id) + "'")
   print(mgmt_eni_id_var)
with open(outfile_vars, 'a') as my_file:
   my_file.write(mgmt_eni_id_var + "\n")


outfile_attach_vmanage_1_nic='attach-vmanage_1-nic.json'
cmd_attach_vmanage_1_nic='aws ec2 attach-network-interface --region' + " " + "{}".format(region) + " " + '--network-interface-id' + " " + "{}".format(mgmt_eni_id) + " " + '--instance-id' + " " + "{}".format(vmanage_1_instance_id) + " " + '--device-index 1'
output = check_output("{}".format(cmd_attach_vmanage_1_nic), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_attach_vmanage_1_nic, 'w') as my_file:
   my_file.write(output)

cmd_associate_eip_mgmt='aws ec2 associate-address --allocation-id' + " " + vmanage_1_index_1_AllocationId + " " + '--network-interface-id' + " " + mgmt_eni_id
print(cmd_associate_eip_mgmt)
output = check_output("{}".format(cmd_associate_eip_mgmt), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
print("Associating eip with the mgmt nic")

#add cluster nic

outfile_add_vmanage_2_nic='add-vmanage_2-nic.json'
cmd_add_vmanage_2_nic='aws ec2 create-network-interface --region' + " " "{}".format(region) + " " + '--subnet-id' + " " + "{}".format(subnetid_cluster) + " " + '--description "vmanage_2_nic_cluster_sub"' + " " + '--groups' + " " + "{}".format(sgid) + " " + "{}".format(priv_sg) + " " + '--tag-specifications' + " " + "'ResourceType=network-interface,Tags=[{Key=Name,Value=" + "{}".format(name) + "index_2" + '}]'"" + "'"
output = check_output("{}".format(cmd_add_vmanage_2_nic), shell=True).decode().strip()
("Creating Secondary NIC on cluster Subne....t")
print("Output: \n{}\n".format(output))
with open(outfile_add_vmanage_2_nic, 'w') as my_file:
    my_file.write(output)


with open(outfile_add_vmanage_2_nic) as access_json:
    read_content = json.load(access_json)
    print(read_content)
    question_access=read_content['NetworkInterface']
    question_data=question_access['NetworkInterfaceId']
    cluster_eni_id=question_data
    cluster_eni_id_var=('eni_id=' + "'" + "{}".format(cluster_eni_id) + "'")
    print(cluster_eni_id_var)
with open(outfile_vars, 'a') as my_file:
    my_file.write(cluster_eni_id_var + "\n")


outfile_attach_vmanage_2_nic='attach-vmanage_2-nic.json'
cmd_attach_vmanage_2_nic='aws ec2 attach-network-interface --region' + " " + "{}".format(region) + " " + '--network-interface-id' + " " + "{}".format(cluster_eni_id) + " " + '--instance-id' + " " + "{}".format(vmanage_1_instance_id) + " " + '--device-index 2'
output = check_output("{}".format(cmd_attach_vmanage_2_nic), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_attach_vmanage_2_nic, 'w') as my_file:
    my_file.write(output)

cmd_associate_eip_cluster='aws ec2 associate-address --allocation-id' + " " + vmanage_1_index_2_AllocationId + " " + '--network-interface-id' + " " + cluster_eni_id
print(cmd_associate_eip_cluster)
output = check_output("{}".format(cmd_associate_eip_cluster), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
print("Associating eip with the cluster nic")

'''
#Add additional SSD of 1 TB to the instance
#Create the volume and get the volume id - /dev/sdf
outfile_volume='volume.json'
cmd_create_volume='aws ec2 create-volume --volume-type gp3 --size 100 --availability-zone' + " " + az + " " + '--tag-specifications' + " " + 'ResourceType=volume,Tags=[{Key=Description,Value=vmanage_1-vol}]'
output = check_output("{}".format(cmd_create_volume), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_volume, 'a') as my_file:
    my_file.write(output + "\n")

with open(outfile_volume) as access_json:
    read_content = json.load(access_json)
    print(read_content)
    question_access=read_content['VolumeId']
    print(question_access)
    vol_id=question_access
    print(vol_id)

#Wait until the volume is read to attach

cmd_check_volume='aws ec2 wait volume-available --volume-ids' + " " + vol_id + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(cmd_check_volume), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#Attach the volume to the instance
#aws ec2 attach-volume --volume-id vol-1234567890abcdef0 --instance-id i-01474ef662b89480 --device /dev/sdf
cmd_attach_vol='aws ec2 attach-volume --volume-id' + " " + vol_id + " " + '--instance-id' + " " + vmanage_1_instance_id + " " + '--device /dev/sdf'
output = check_output("{}".format(cmd_attach_vol), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
'''

#Wait to check the instance is initialized
#Check that the instance is initialized
cmd_check_instance='aws ec2 wait instance-status-ok --instance-ids' + " " + vmanage_1_instance_id + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(cmd_check_instance), shell=True).decode().strip()
print("Output: \n{}\n".format(output))



#write the insance_id to the vault
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_1" + "/" + "vmanage_1_instance_id"
print(url)

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"vmanage_1_instance_id": vmanage_1_instance_id }

resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#Write the index0 and  Network Card IDs to the Vault
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_1" + "/" + "pub_eni_id"
print(url)

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"pub_eni_id": pub_eni_id }

resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#Write the index1 and  Network Card IDs to the Vault
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_1" + "/" + "mgmt_eni_id"
print(url)

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"mgmt_eni_id": mgmt_eni_id }

resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)


#Write the index2 and  Network Card IDs to the Vault
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_1" + "/" + "cluster_eni_id"
print(url)

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"cluster_eni_id": cluster_eni_id }

resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

'''
#Write the volume ID to the vault
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vmanage_1" + "/" + "vol_id"
print(url)

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"vol_id": vol_id }

resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)
'''