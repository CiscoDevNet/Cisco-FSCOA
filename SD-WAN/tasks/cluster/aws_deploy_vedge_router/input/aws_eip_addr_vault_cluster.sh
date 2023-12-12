#!/bin/sh
export AWS_PAGER=""
#This is required for vault
setcap cap_ipc_lock= /usr/bin/vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $VAULT_TOKEN
export AWS_PAGER=""
export Name=$NAME
echo $NAME
aws configure set aws_access_key_id $AWS_KEY_ID
aws configure set aws_secret_access_key $AWS_KEY
aws configure set default.region $REGION

set x

#This retrieves the EIPs from the vault and sets them as environmental variables for python to call in the build container

#Retrieves the EIP allocation IDs from vault for each instance type, eni index
#vedge_1
export vedge_1_index_0_AllocationId=$(vault kv get --field=vedge_1_index_0_AllocationId concourse/sdwan/$NAME/vedge_1_index_0_AllocationId)
export vedge_1_index_1_AllocationId=$(vault kv get --field=vedge_1_index_1_AllocationId concourse/sdwan/$NAME/vedge_1_index_1_AllocationId)

#vedge
export vedge_1_index_0_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vedge_1_index_0_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vedge_1_index_1_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vedge_1_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")


#Public IPs
#vedge
echo "vedge_1_index_0_pub_ip"
echo $vedge_1_index_0_pub_ip
echo "vedge_1_index_1_pub_ip"
echo $vedge_1_index_1_pub_ip

cd input
#Remember to Refactor in order to hard code the internal IPs as static just for the lab so each student has exact same IPs on same interface
python3 aws_eip_addr_vault_cluster.py
