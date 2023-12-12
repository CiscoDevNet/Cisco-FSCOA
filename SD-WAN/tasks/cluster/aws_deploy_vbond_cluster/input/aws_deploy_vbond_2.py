#!/usr/bin/env python
#This Script creates the vbond_2 from AMI and the key - split out the key
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

ami_id= os.getenv('ami_id')
sgid = os.getenv('sgid')
print(sgid)
vpcid = os.getenv('vpcid')
subnetid_mgmt = os.getenv('subnetid_mgmt')
subnetid_public = os.getenv('subnetid_public')


instance_type='c5.4xlarge'
outfile_deploy_vbond_2='deploy-vbond_2.json'
outfile_get_vpcid='outfile_get_vpcid.json'

inst_name="vbond_2"
sg_name=name
priv_sg = os.getenv('priv_sg')
vbond_2_index_0_AllocationId = os.getenv('vbond_2_index_0_AllocationId')
vbond_2_index_1_AllocationId = os.getenv('vbond_2_index_1_AllocationId')


cmd_deploy_vbond_2='aws ec2 run-instances --region' + " " + "{}".format(region) + " " + '--image-id' + " " + "{}".format(ami_id) + " " + '--instance-type' + " " + "{}".format(instance_type) + " " + '--subnet-id' + " " + "{}".format(subnetid_mgmt) +  " " + '--security-group-ids' + " " + "{}".format(sgid) + " " + "{}".format(priv_sg) + " " + '--placement AvailabilityZone=' + "{}".format(az) + " " + '--user-data file://vbond_user_data'
output = check_output("{}".format(cmd_deploy_vbond_2), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

with open(outfile_deploy_vbond_2, 'w') as my_file:
    my_file.write(output)

with open (outfile_deploy_vbond_2) as access_json:
    read_content = json.load(access_json)
    question_access_vbond_2 = read_content['Instances']
    replies_access_vbond_2 = question_access_vbond_2[0]
    replies_data_vbond_2=replies_access_vbond_2['InstanceId']
    print(replies_data_vbond_2)
    vbond_2_instance_id=replies_data_vbond_2 #add this to the vars file
    print(vbond_2_instance_id)
    vbond_2_instance_id_var=('vbond_2_instance_id=' + "'" + "{}".format(vbond_2_instance_id) + "'")
    vbond_2_int_ip_addr=replies_access_vbond_2['PrivateIpAddress']
    print(vbond_2_int_ip_addr)

with open(outfile_vars, 'a+') as my_file:
    my_file.write(vbond_2_instance_id_var + "\n")

vbond_2_instance_id_var=('vbond_2_instance_id=' + "'" + "{}".format(vbond_2_instance_id) + "'")
print(vbond_2_instance_id_var)
with open(outfile_vars, 'a') as my_file:
    my_file.write(vbond_2_instance_id_var + "\n")

vbond_2_tag_inst='aws ec2 create-tags --region' + " " + "{}".format(region) + " " + '--resources' + " " +  "{}".format(vbond_2_instance_id) + " " + '--tags' + " " + "'" + 'Key="Name",Value=vbond_2' + "'"
output = check_output("{}".format(vbond_2_tag_inst), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

cmd_vbond_2_mgmt_eni_id='aws ec2 describe-instances --instance-id' + " " + vbond_2_instance_id + " " + '--query' + " " + 'Reservations[].Instances[].NetworkInterfaces[*].NetworkInterfaceId'
print(cmd_vbond_2_mgmt_eni_id)
output = check_output("{}".format(cmd_vbond_2_mgmt_eni_id), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

outfile_get_mgmt_eni_id='outfile_get_mgmt_eni_id.json'
with open(outfile_get_mgmt_eni_id, 'w') as my_file:
    my_file.write(output)
with open (outfile_get_mgmt_eni_id) as access_json:
    read_content = json.load(access_json)
    print(read_content)
    question_access = read_content[0]
    print(question_access)
    mgmt_eni_id=question_access[0]
    print(mgmt_eni_id)

cmd_check_instance='aws ec2 wait instance-running --instance-ids' + " " + vbond_2_instance_id + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(cmd_check_instance), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

cmd_associate_eip_mgmt='aws ec2 associate-address --allocation-id' + " " + "{}".format(vbond_2_index_0_AllocationId) + " " + '--network-interface-id' + " " + mgmt_eni_id
print(cmd_associate_eip_mgmt)
output = check_output("{}".format(cmd_associate_eip_mgmt), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
print("Associating eip with the mgmt nic")

#Create Secondary NIC
outfile_add_vbond_2_nic='add-vbond_2-nic.json'
cmd_add_vbond_2_nic='aws ec2 create-network-interface --region' + " " "{}".format(region) + " " + '--subnet-id' + " " + "{}".format(subnetid_public) + " " + '--description "vbond_2_nic_pub_sub"' + " " + '--groups' + " " + "{}".format(sgid) + " " + "{}".format(priv_sg) + " " + '--tag-specifications' + " " + "'ResourceType=network-interface,Tags=[{Key=Name,Value=" + "{}".format(inst_name) + "_" + "index_1" + '}]'"" + "'"
output = check_output("{}".format(cmd_add_vbond_2_nic), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_add_vbond_2_nic, 'w') as my_file:
    my_file.write(output)


with open(outfile_add_vbond_2_nic) as access_json:
    read_content = json.load(access_json)
    print(read_content)
    question_access=read_content['NetworkInterface']
    question_data=question_access['NetworkInterfaceId']
    pub_eni_id=question_data
    pub_eni_id_var=('eni_id=' + "'" + "{}".format(pub_eni_id) + "'")
    print(pub_eni_id_var)
with open(outfile_vars, 'a') as my_file:
    my_file.write(pub_eni_id_var + "\n")


outfile_attach_vbond_2_nic='attach-vbond_2-nic.json'
cmd_attach_vbond_2_nic='aws ec2 attach-network-interface --region' + " " + "{}".format(region) + " " + '--network-interface-id' + " " + "{}".format(pub_eni_id) + " " + '--instance-id' + " " + "{}".format(vbond_2_instance_id) + " " + '--device-index 1'
output = check_output("{}".format(cmd_attach_vbond_2_nic), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_attach_vbond_2_nic, 'w') as my_file:
    my_file.write(output)

cmd_associate_eip_pub='aws ec2 associate-address --allocation-id' + " " + vbond_2_index_1_AllocationId + " " + '--network-interface-id' + " " + pub_eni_id
print(cmd_associate_eip_pub)
output = check_output("{}".format(cmd_associate_eip_pub), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
print("Associating eip with the pub nic")

cmd_associate_eip_mgmt='aws ec2 associate-address --allocation-id' + " " + vbond_2_index_0_AllocationId + " " + '--network-interface-id' + " " + mgmt_eni_id
print(cmd_associate_eip_mgmt)
output = check_output("{}".format(cmd_associate_eip_mgmt), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
print("Associating eip with the mgmt nic")

'''
#Add additional SSD of 1 TB to the instance
#Create the volume and get the volume id - /dev/sdf
outfile_volume='volume.json'
cmd_create_volume='aws ec2 create-volume --volume-type gp2 --size 100 --availability-zone' + " " + az + " " + '--tag-specifications' + " " + 'ResourceType=volume,Tags=[{Key=Description,Value=vbond_2-vol}]'
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
cmd_attach_vol='aws ec2 attach-volume --volume-id' + " " + vol_id + " " + '--instance-id' + " " + vbond_2_instance_id + " " + '--device /dev/sdf'
output = check_output("{}".format(cmd_attach_vol), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
'''

#Wait to check the instance is initialized
#Check that the instance is initialized
cmd_check_instance='aws ec2 wait instance-status-ok --instance-ids' + " " + vbond_2_instance_id + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(cmd_check_instance), shell=True).decode().strip()
print("Output: \n{}\n".format(output))



#write the insance_id to the vault
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vbond_2" + "/" + "vbond_2_instance_id"
print(url)

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"vbond_2_instance_id": vbond_2_instance_id }

resp = requests.post(url, headers=headers, json=data_json)
print(resp)
print(resp.status_code)
print(name)

#Write the Secondary and Tertiary Network Card IDs to the Vault
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vbond_2" + "/" + "pub_eni_id"
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

'''
#Write the volume ID to the vault
url = "http://prod-vault.devops-ontap.com:8200/v1/concourse/sdwan/" + name + "/" + "vbond_2" + "/" + "vol_id"
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