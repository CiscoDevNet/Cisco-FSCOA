#!/bin/sh
apt-get update
apt-get -y install python3-pip --fix-missing
/usr/local/bin/python -m pip install --upgrade pip
cd git-resource/tasks/cluster/aws_configure_vsmart_cluster/input
pip3 install netmiko
#Login to vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $VAULT_TOKEN
#get the private key
vault kv get --field=ssh-key concourse/sdwan/ssh-ed25519-private-key >> vmanage.pem
chmod 400 vmanage.pem
#vsmart_1
export vsmart_1_index_0_pub_ip=$(vault kv get --field=vsmart_1_index_0_pub_ip concourse/sdwan/$NAME/vsmart_1_index_0_pub_ip)
python3 configure_vsmart_1_ssh.py
