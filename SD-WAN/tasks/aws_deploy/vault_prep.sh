#!/bin/sh
export AWS_PAGER=""
#This is required for vault
setcap cap_ipc_lock= /usr/bin/vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
echo $VAULT_TOKEN
vault login --no-print $VAULT_TOKEN
vault kv list concourse/sdwan
#python3 vault_prep.py







