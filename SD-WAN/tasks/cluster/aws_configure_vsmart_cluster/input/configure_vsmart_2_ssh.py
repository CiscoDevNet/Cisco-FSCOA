#!/usr/bin/env python
import json, re, sys, os, json, subprocess
from subprocess import call, check_output
import netmiko
from netmiko import *


from netmiko import ConnectHandler

key_file='vmanage.pem'
username='admin'

ip = os.getenv('vsmart_2_index_0_pub_ip')
print(ip)

net_connect = netmiko.ConnectHandler(ip=ip, device_type="cisco_viptela", username="admin", password="admin", key_file=key_file)

output= net_connect.send_config_set("system")
print(output)

output= net_connect.send_config_set("host-name vsmart_2")
print(output)

output= net_connect.send_config_set("site-id 1")
print(output)

output= net_connect.send_config_set("system-ip 172.16.1.114")
print(output)

#Org Name Must Match what was set in the Licensing on Cisco Licensing
output= net_connect.send_config_set("organization-name devops-ontap.com")
print(output)

output= net_connect.send_config_set("vbond vbond.devops-ontap.com")
print(output)

output= net_connect.send_config_set("vpn 0")
print(output)

output = net_connect.send_config_set("no interface eth0")
print(output)

output = net_connect.send_config_set("interface eth1")
print(output)

output = net_connect.send_config_set("no shut")
print(output)

output = net_connect.send_config_set("ip dhcp-client")
print(output)

output = net_connect.send_config_set("tunnel-interface")
print(output)

output = net_connect.send_config_set("allow-service all")
print(output)

output = net_connect.send_config_set("allow-service netconf")
print(output)

output = net_connect.send_config_set("exit")
print(output)

output = net_connect.send_config_set("exit")
print(output)

output = net_connect.send_config_set("exit")
print(output)

output = net_connect.send_config_set("vpn 512")
print(output)

output = net_connect.send_config_set("interface eth0")
print(output)

output = net_connect.send_config_set("ip dhcp-client")
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

output= net_connect.send_command("sh int | t")
print(output)

output= net_connect.send_command("sh run")
print(output)

output = net_connect.send_config_set("exit")
print(output)