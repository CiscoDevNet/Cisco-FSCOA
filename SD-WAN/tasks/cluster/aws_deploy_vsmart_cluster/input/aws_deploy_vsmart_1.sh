#!/bin/sh
export AWS_PAGER=""
rm -rf __pycache__
export NAME=$NAME
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $VAULT_TOKEN
export vpcid=$(vault kv get --field=vpcid concourse/sdwan/$NAME/vpcid)
echo $vpcid
export sgid=$(vault kv get --field=SDWAN_sg_id concourse/sdwan/$NAME/SDWAN_sg_id)
echo "security group id...."
echo $sgid
export ami_id='ami-0b7f988dd9b328b3d'
export priv_sg=$(vault kv get --field=SDWAN_priv_sg_id concourse/sdwan/$NAME/SDWAN_priv_sg_id)
export subnetid_mgmt=$(vault kv get --field=subnetid_mgmt concourse/sdwan/$NAME/subnetid_mgmt)
export subnetid_public=$(vault kv get --field=subnetid_public concourse/sdwan/$NAME/subnetid_public)
export vsmart_1_index_0_AllocationId=$(vault kv get --field=vsmart_1_index_0_AllocationId concourse/sdwan/$NAME/vsmart_1_index_0_AllocationId)
echo $vsmart_1_index_0_AllocationId
export vsmart_1_index_1_AllocationId=$(vault kv get --field=vsmart_1_index_1_AllocationId concourse/sdwan/$NAME/vsmart_1_index_1_AllocationId)
cd git-resource/tasks/cluster/aws_deploy_vsmart_cluster/input
python3 aws_deploy_vsmart_1.py
