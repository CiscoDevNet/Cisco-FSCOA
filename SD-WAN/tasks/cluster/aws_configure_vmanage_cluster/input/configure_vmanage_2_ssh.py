#!/usr/bin/env python
import json, re, sys, os, json, subprocess
from subprocess import call, check_output
import netmiko
from netmiko import *
from netmiko import ConnectHandler

key_file='vmanage.pem'
username='admin'

ip = os.getenv('vmanage_2_index_0_pub_ip')
print(ip)

net_connect = netmiko.ConnectHandler(ip=ip, device_type="cisco_viptela", username="admin", password="admin", key_file=key_file)
print(net_connect.send_command("request nms all status"))

print(net_connect.send_command("show run"))


output= net_connect.send_config_set("system")
print(output)


output= net_connect.send_config_set("host-name vmanage_2")
print(output)


output= net_connect.send_config_set("system-ip 172.16.1.12")
print(output)

output= net_connect.send_config_set("site-id 1")
print(output)

output= net_connect.send_config_set("organization-name devops-ontap.com")
print(output)

output= net_connect.send_config_set("vbond vbond.devops-ontap.com")
print(output)

output= net_connect.send_config_set("vpn 0")
print(output)

output = net_connect.send_config_set("no interface eth2")

output = net_connect.send_config_set("no interface eth1")

output = net_connect.send_config_set("interface eth0")


output = net_connect.send_config_set("no shut")
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

output = net_connect.send_config_set("interface eth2")
print(output)

output = net_connect.send_config_set("ip dhcp-client")
print(output)

output = net_connect.send_config_set("no shut")
print(output)

output = net_connect.send_config_set("exit")
print(output)

output = net_connect.send_config_set("exit")
print(output)

output= net_connect.send_config_set("vpn 512")
print(output)

output = net_connect.send_config_set("interface eth1")
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

output = net_connect.send_config_set("exit")
print(output)

