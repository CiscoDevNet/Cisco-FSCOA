#!/bin/sh
apt-get update
apt-get -y install python3-pip --fix-missing
python3 -m pip install --upgrade pip
cd input
pip3 install netmiko
#Login to vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $VAULT_TOKEN
#get the private key
vault kv get --field=ssh-key concourse/sdwan/ssh-ed25519-private-key >> vmanage.pem
chmod 400 vmanage.pem
export vedge_1_index_0_pub_ip=$(vault kv get --field=vedge_1_index_0_pub_ip concourse/sdwan/$NAME/vedge_1_index_0_pub_ip)
python3 configure_vedge_1_ssh.py