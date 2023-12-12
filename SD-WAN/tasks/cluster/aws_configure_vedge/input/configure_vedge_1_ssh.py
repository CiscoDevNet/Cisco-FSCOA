#!/usr/bin/env python
import json, re, sys, os, json, subprocess
from subprocess import call, check_output
import netmiko
from netmiko import *


from netmiko import ConnectHandler

key_file='vmanage.pem'
username='admin'

ip = os.getenv('vedge_1_index_0_pub_ip')
print(ip)

net_connect = netmiko.ConnectHandler(ip=ip, device_type="cisco_viptela", username="admin", password="admin" ,key_file=key_file)
print(net_connect.send_command("request nms all status"))

print(net_connect.send_command("show run"))

output= net_connect.send_config_set("conf t")
print(output)

output= net_connect.send_config_set("system")
print(output)

output= net_connect.send_config_set("host-name vedge_1")
print(output)

output= net_connect.send_config_set("site-id 1")
print(output)

output= net_connect.send_config_set("system-ip 172.16.1.115")
print(output)

#Org Name Must Match what was set in the Licensing on Cisco Licensing
output= net_connect.send_config_set("organization-name devops-ontap.com-aspadescisco")
print(output)

output= net_connect.send_config_set("sp-organization-name devops-ontap.com")
print(output)

output= net_connect.send_config_set("vbond vbond.devops-ontap.com")
print(output)

output= net_connect.send_config_set("exit")
print(output)

output= net_connect.send_config_set("vpn 0")
print(output)


output = net_connect.send_config_set("interface ge0/0")
print(output)


output = net_connect.send_config_set("no shut")
print(output)

output = net_connect.send_config_set("tunnel-interface")
print(output)

output = net_connect.send_config_set("encapsulation ipsec")
print(output)

output = net_connect.send_config_set("color biz-internet")
print(output)

output = net_connect.send_config_set("allow-service all")
print(output)

output = net_connect.send_config_set("allow-service netconf")
print(output)

output = net_connect.send_config_set("no shut")
print(output)

output = net_connect.send_config_set("exit")
print(output)

output = net_connect.send_config_set("exit")
print(output)

output = net_connect.send_config_set("commit")
print(output)

output = net_connect.send_config_set("exit")
print(output)

output = net_connect.send_config_set("exit")
print(output)

output= net_connect.send_config_set("exit")
print(output)

print(net_connect.send_command("show run"))

output= net_connect.send_config_set("exit")
print(output)

