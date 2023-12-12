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
#vmanage_1
export vmanage_1_index_0_AllocationId=$(vault kv get --field=vmanage_1_index_0_AllocationId concourse/sdwan/$NAME/vmanage_1_index_0_AllocationId)
export vmanage_1_index_1_AllocationId=$(vault kv get --field=vmanage_1_index_1_AllocationId concourse/sdwan/$NAME/vmanage_1_index_1_AllocationId)
export vmanage_1_index_2_AllocationId=$(vault kv get --field=vmanage_1_index_2_AllocationId concourse/sdwan/$NAME/vmanage_1_index_2_AllocationId)

#vmanage_2
export vmanage_2_index_0_AllocationId=$(vault kv get --field=vmanage_2_index_0_AllocationId concourse/sdwan/$NAME/vmanage_2_index_0_AllocationId)
export vmanage_2_index_1_AllocationId=$(vault kv get --field=vmanage_2_index_1_AllocationId concourse/sdwan/$NAME/vmanage_2_index_1_AllocationId)
export vmanage_2_index_2_AllocationId=$(vault kv get --field=vmanage_2_index_2_AllocationId concourse/sdwan/$NAME/vmanage_2_index_2_AllocationId)

#vmanage_3
export vmanage_3_index_0_AllocationId=$(vault kv get --field=vmanage_3_index_0_AllocationId concourse/sdwan/$NAME/vmanage_3_index_0_AllocationId)
export vmanage_3_index_1_AllocationId=$(vault kv get --field=vmanage_3_index_1_AllocationId concourse/sdwan/$NAME/vmanage_3_index_1_AllocationId)
export vmanage_3_index_2_AllocationId=$(vault kv get --field=vmanage_3_index_2_AllocationId concourse/sdwan/$NAME/vmanage_3_index_2_AllocationId)

#vbond_1
export vbond_1_index_0_AllocationId=$(vault kv get --field=vbond_1_index_0_AllocationId concourse/sdwan/$NAME/vbond_1_index_0_AllocationId)
export vbond_1_index_1_AllocationId=$(vault kv get --field=vbond_1_index_1_AllocationId concourse/sdwan/$NAME/vbond_1_index_1_AllocationId)

#vbond_2
export vbond_2_index_0_AllocationId=$(vault kv get --field=vbond_2_index_0_AllocationId concourse/sdwan/$NAME/vbond_2_index_0_AllocationId)
export vbond_2_index_1_AllocationId=$(vault kv get --field=vbond_2_index_1_AllocationId concourse/sdwan/$NAME/vbond_2_index_1_AllocationId)

#vsmart_1
export vsmart_1_index_0_AllocationId=$(vault kv get --field=vsmart_1_index_0_AllocationId concourse/sdwan/$NAME/vsmart_1_index_0_AllocationId)
export vsmart_1_index_1_AllocationId=$(vault kv get --field=vsmart_1_index_1_AllocationId concourse/sdwan/$NAME/vsmart_1_index_1_AllocationId)

#vsmart_2
export vsmart_2_index_0_AllocationId=$(vault kv get --field=vsmart_2_index_0_AllocationId concourse/sdwan/$NAME/vsmart_2_index_0_AllocationId)
export vsmart_2_index_1_AllocationId=$(vault kv get --field=vsmart_2_index_1_AllocationId concourse/sdwan/$NAME/vsmart_2_index_1_AllocationId)

#vedge_1
export vedge_1_index_0_AllocationId=$(vault kv get --field=vedge_1_index_0_AllocationId concourse/sdwan/$NAME/vedge_1_index_0_AllocationId)
export vedge_1_index_1_AllocationId=$(vault kv get --field=vedge_1_index_1_AllocationId concourse/sdwan/$NAME/vedge_1_index_1_AllocationId)

#exports to env var the public IP for the specific EIP values retrieved from vault
#vmanage_1
export vmanage_1_index_0_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vmanage_1_index_0_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vmanage_1_index_1_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vmanage_1_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vmanage_1_index_2_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vmanage_1_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
#vmanage_2
export vmanage_2_index_0_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vmanage_2_index_0_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vmanage_2_index_1_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vmanage_2_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vmanage_2_index_2_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vmanage_2_index_2_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
#vmanage_3
export vmanage_3_index_0_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vmanage_3_index_0_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vmanage_3_index_1_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vmanage_3_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vmanage_3_index_2_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vmanage_3_index_2_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
#vbond_1
export vbond_1_index_0_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vbond_1_index_0_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vbond_1_index_1_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vbond_1_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
#vbond_2
export vbond_2_index_0_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vbond_2_index_0_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vbond_2_index_1_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vbond_2_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
#vsmart_1
export vsmart_1_index_0_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vsmart_1_index_0_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vsmart_1_index_1_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vsmart_1_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
#vsmart_2
export vsmart_2_index_0_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vsmart_2_index_0_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vsmart_2_index_1_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vsmart_2_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
#vedge
export vedge_1_index_0_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vedge_1_index_0_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")
export vedge_1_index_1_pub_ip=$(aws ec2 describe-addresses --region us-west-2 --allocation-ids $vedge_1_index_1_AllocationId --query "Addresses[0].[PublicIp] | [0]" | tr -d "\"")


#Public IPs
#vmanage_1
echo "vmanage_1_index_0_pub_ip"
echo $vmanage_1_index_0_pub_ip
echo "vmanage_1_index_1_pub_ip"
echo $vmanage_1_index_1_pub_ip
echo "vmanage_1_index_2_pub_ip"
echo $vmanage_1_index_2_pub_ip
#vmanage_2
echo "vmanage_2_index_0_pub_ip"
echo $vmanage_2_index_0_pub_ip
echo "vmanage_2_index_1_pub_ip"
echo $vmanage_2_index_1_pub_ip
echo "vmanage_2_index_2_pub_ip"
echo $vmanage_2_index_2_pub_ip
#vmanage_3
echo "vmanage_3_index_0_pub_ip"
echo $vmanage_3_index_0_pub_ip
echo "vmanage_3_index_1_pub_ip"
echo $vmanage_3_index_1_pub_ip
echo "vmanage_3_index_2_pub_ip"
echo $vmanage_3_index_2_pub_ip

#vbond_1
echo "vbond_1_index_0_pub_ip"
echo $vbond_1_index_0_pub_ip
echo "vbond_1_index_1_pub_ip"
echo $vbond_1_index_1_pub_ip
#vbond_2
echo "vbond_2_index_0_pub_ip"
echo $vbond_2_index_0_pub_ip
echo "vbond_2_index_1_pub_ip"
echo $vbond_2_index_1_pub_ip
#vbond3
echo "vbond3_index_0_pub_ip"
echo $vbond3_index_0_pub_ip
echo "vbond3_index_1_pub_ip"
echo $vbond3_index_1_pub_ip

#vsmart_1
echo "vsmart_1_index_0_pub_ip"
echo $vsmart_1_index_0_pub_ip
echo "vsmart_1_index_1_pub_ip"
echo $vsmart_1_index_1_pub_ip
#vsmart_2
echo "vsmart_2_index_0_pub_ip"
echo $vsmart_2_index_0_pub_ip
echo "vsmart_2_index_1_pub_ip"
echo $vsmart_2_index_1_pub_ip

#vedge
echo "vedge_1_index_0_pub_ip"
echo $vedge_1_index_0_pub_ip
echo "vedge_1_index_1_pub_ip"
echo $vedge_1_index_1_pub_ip

cd git-resource/tasks/cluster/aws_deploy_eips_cluster/input/vault
#Remember to Refactor in order to hard code the internal IPs as static just for the lab so each student has exact same IPs on same interface
python3 aws_eip_addr_vault_cluster.py
