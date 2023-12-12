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
#export AWS_KEY_ID=$(vault kv get --field=Access_key concourse/main/Access_key_ID)
#export AWS_KEY=$(vault kv get --field=Secret_access_key concourse/main/Secret_access_key)
aws configure set aws_access_key_id $AWS_KEY_ID
aws configure set aws_secret_access_key $AWS_KEY
aws configure set default.region $REGION

cd git-resource/tasks/cluster/aws_deploy_eips_cluster/input/vbond
python3 aws_deploy_eips_cluster_vbond_2.py






