#!/bin/sh
echo "testing new version of build container"
echo "checking if netmiko is installed"
pip3 install netmiko
pip list | grep netmiko
pip3 list | grep netmiko
#Login to vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $VAULT_TOKEN
cd git-resource/tasks/cluster/aws_configure_vmanage_cluster/input
#get the private key
vault kv get --field=ssh-key concourse/sdwan/ssh-ed25519-private-key >> vmanage.pem
chmod 400 vmanage.pem
#vmanage_2
export vmanage_2_index_0_pub_ip=$(vault kv get --field=vmanage_2_index_0_pub_ip concourse/sdwan/$NAME/vmanage_2_index_0_pub_ip)
echo $vmanage_2_index_0_pub_ip
python3 configure_vmanage_2_ssh.py

