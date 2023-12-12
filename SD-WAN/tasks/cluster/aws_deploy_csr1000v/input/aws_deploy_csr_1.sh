#!/bin/sh
export AWS_PAGER=""
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
export priv_sg=$(vault kv get --field=SDWAN_priv_sg_id concourse/sdwan/$NAME/SDWAN_priv_sg_id)
export subnetid_mgmt=$(vault kv get --field=subnetid_mgmt concourse/sdwan/$NAME/subnetid_mgmt)
export subnetid_public=$(vault kv get --field=subnetid_public concourse/sdwan/$NAME/subnetid_public)
export csr1000v_1_index_0_AllocationId=$(vault kv get --field=csr1000v_1_index_0_AllocationId concourse/sdwan/$NAME/csr1000v_1_index_0_AllocationId)
echo $csr1000v_1_index_0_AllocationId
export csr1000v_1_index_1_AllocationId=$(vault kv get --field=csr1000v_1_index_1_AllocationId concourse/sdwan/$NAME/csr1000v_1_index_1_AllocationId)
cd input
python3 aws_deploy_csr_1.py

