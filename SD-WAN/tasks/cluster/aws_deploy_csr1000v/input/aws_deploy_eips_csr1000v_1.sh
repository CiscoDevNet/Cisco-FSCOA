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
cd input
python3 aws_deploy_eips_csr1000v_1.py






