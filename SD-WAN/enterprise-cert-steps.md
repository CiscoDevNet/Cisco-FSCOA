Eenteprise root ca pem and key
=====

How the Vedge Router Authenticates to Vmanage, Vsmart and Vbond
=================
https://www.cisco.com/c/en/us/td/docs/routers/sdwan/configuration/sdwan-xe-gs-book/cisco-sd-wan-overlay-network-bringup.html?bookSearch=true





aspadescisco

update the A record for vbond.devops-ontap.com with the public internal IP 

openssl genrsa -out ROOT-CA.key 2048

openssl req -x509 -new --nodes -key ROOT-CA.key -sha256 -days 3652 -subj "/C=US/ST=CA/L=SanJose/O=devops-ontap.com/CN=devops-ontap.com" -out ROOT-CA.pem

openssl req -x509 -new --nodes -key ROOT-CA.key -sha256 -days 3652 -subj "/C=US/ST=CA/L=SanJose/O=devops-ontap.com/CN=devops-ontap.com" -out ROOT-CA.pem
request root-cert-chain install /home/admin/ROOT-CA.pem

Install the pem in the gui then generate the CSR 
======

Configuration > Certificates > Controllers > vManage > Generate CSR:configuration, certificates, controllers, click on 3 dots and select generate csr. This pushes a csr to the machine.
Use the CSR to generate the CRT and then select on same page in GUI "Install Certificate"

generate the crt
=====
openssl x509 -req -in vmanage_csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vmanage.crt -days 1826 -sha256

Install crt in the gui
=============

from vbond, smart, vedge
============

request download scp://admin@184.169.141.21:/home/admin/ROOT-CA.pem 

request root-cert-chain install /home/admin/ROOT-CA.pem 


Add each controller in the GUI
======
This automatically generates a CSR and pushes it to those machines


Copy the csrs from vbond and vsmart to the vmanage to create the crt
==========
scp admin@10.100.1.86:/home/admin/vmanage_csr ./vmanage_2_csr
scp admin@10.100.1.27:/home/admin/vmanage_csr ./vmanage_3_csr


scp admin@10.100.1.228:/home/admin/vbond_csr ./vbond_1_csr
scp admin@10.100.1.193:/home/admin/vbond_csr ./vbond_2_csr

scp admin@10.100.1.54:/home/admin/vsmart_csr ./vmsart_1_csr
scp admin@10.100.1.98:/home/admin/vsmart_csr ./vsmart_2_csr

184.169.141.21
scp admin@184.169.141.21:/home/admin/edge_1_csr ./vedge_1.csr

from vmanage create the CRT for vbond and vsmart and copy them into the gui
=========
openssl x509 -req -in vmanage_1.csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vmanage_1.crt -days 1826 -sha256
openssl x509 -req -in vmanage_2.csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vmanage_2.crt -days 1826 -sha256
openssl x509 -req -in vmanage_3_csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vmanage_3.crt -days 1826 -sha256

openssl x509 -req -in vbond_1.csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vbond_1.crt -days 1826 -sha256
openssl x509 -req -in vbond_2.csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vbond_2.crt -days 1826 -sha256

openssl x509 -req -in vsmart_1.csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vsmart_1.crt -days 1826 -sha256
openssl x509 -req -in vsmart_2.csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vsmart_2.crt -days 1826 -sha256

openssl x509 -req -in vedge_1.csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vedge_1.crt -days 1826 -sha256

openssl x509 -req -in vedge_cloud_csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vedge_cloud.crt -days 1826 -sha256

From vedge only
=======
request csr upload home/admin/vedge_1.csr
(this creates a csr request on the vedge server)

it prompts for the organization name twice - devops-ontap.com-aspadescisco

from vmanage - copy up the CSR to create the crt
=====
scp admin@10.100.1.201:/home/admin/vbond_csr .

scp admin@10.100.1.4
9:/home/admin/vsmart_csr .

scp admin@54.215.35.80:/home/admin/vedge_1.csr .

Create the CRT on vmanage
=======
openssl x509 -req -in vedge_1.csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vedge_1.crt -days 1826 -sha256

openssl x509 -req -in vbond_csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vbond.crt -days 1826 -sha256

openssl x509 -req -in vsmart_csr -CA ROOT-CA.pem -CAkey ROOT-CA.key -CAcreateserial -out vsmart.crt -days 1826 -sha256


From vedge request the crt from vmanage
=====


vedge
=====
scp admin@184.169.141.21:/home/admin/vedge_1.crt .


From vedge request the crt from vmanage
======

request download scp://184.169.141.21:/home/admin/vedge_1.crt
request certificate install home/admin/vedge_1.crt 

Import vedge to the vmanage
======

Get the chassis number:
show certificate serial

Chassis number: f39f33d5-da7c-4f78-bdb9-930126ecf3a6 serial number: 5BA51CB888793D98B1A5621B7BCCE63B2CEEAD73




Run this on both vmanage and vbond
=======

request vedge add chassis-num 6ef7f976-2bd4-4c7c-a770-3c31d5c86494  serial-num 18831d361bc945a3a3c5e89bfd47716a

On vbond
===
request vedge add chassis-num 6ef7f976-2bd4-4c7c-a770-3c31d5c86494 serial-num 18831d361bc945a3a3c5e89bfd47716a


Chassis number: f39f33d5-da7c-4f78-bdb9-930126ecf3a6 serial number: 5BA51CB888793D98B1A5621B7BCCE63B2CEEAD72

Send To Controllers
=======
configuration>certificates>wan edge list
select send to controllers 


This may be required
=====
request vedge-cloud activate chassis-number fd920820-234f-4c67-232b-e6d7fc8ea334 token c61e7749c0fe46529f881051965671d2

from vbond
======

request vedge-cloud activate chassis-number 6cc9835b-fcef-5a5c-4fc6-87e1b630d7df token 18831d361bc945a3a3c5e89bfd47716a

request vedge-cloud activate chassis-number 6d938b1eb2224b47b91a6b925a30a5de token 6d938b1eb2224b47b91a6b925a30a5de

==========
request nms all status  
request nms application-server status
request nms application-server restart
request nms application-server start

========

show control connections-history
show clock
show orchestrator connections-history (from vbond)

vedge
request vedge-cloud activate chassis-number 6cc9835b-fcef-5a5c-4fc6-87e1b630d7df token 18831d361bc945a3a3c5e89bfd47716a