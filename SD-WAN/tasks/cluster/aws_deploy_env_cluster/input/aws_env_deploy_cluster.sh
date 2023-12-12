#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
cd git-resource/tasks/cluster/aws_deploy_env_cluster/input
python3 aws_env_deploy_cluster.py
