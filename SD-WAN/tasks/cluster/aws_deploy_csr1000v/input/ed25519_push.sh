#!/bin/sh
export AWS_PAGER=""
#This is required for vault
setcap cap_ipc_lock= /usr/bin/vault
export NAME=$NAME
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $VAULT_TOKEN
cd git-resource tasks/cluster/push_ed25519_public_key_cluster/input
#read the ed25519 key and push it to all the instances.
#Get the EDSA priv and pub key from vault and set as env vars to be used in python script that will use AWS CLI to copy them up
#vault kv get --field=ssh-key concourse/sdwan/$NAME/ssh-ed25529-private-key >> ed25519
vault kv get --field=ssh-key concourse/sdwan/ssh-ed25519-public-key >> ed25519.pub
#vault kv get --field=vmanage_user_data concourse/sdwan/vmanage_user_data >> /git-resource/tasks/aws_deploy/vmanage_user_data
#copy the public key to each instance - get the instance_id for each of the 3 instances from the  vault
#vmanage_1
echo "vmanage_1"
vault kv get --field=vmanage_1_instance_id concourse/sdwan/$NAME/vmanage_1/vmanage_1_instance_id >> vmanage_1_instance_id
export VMANAGE_1_INSTANCE_ID=$(cat vmanage_1_instance_id)
aws ec2-instance-connect send-serial-console-ssh-public-key --instance-id $VMANAGE_1_INSTANCE_ID --serial-port 0 --ssh-public-key file://ed25519.pub --region $REGION
echo $VMANAGE_1_INSTANCE_ID
#vmanage_2
echo "vmanage_2"
echo$VMANAGE_2_INSTANCE_ID
vault kv get --field=vmanage_2_instance_id concourse/sdwan/$NAME/vmanage_2/vmanage_2_instance_id >> vmanage_2_instance_id
export VMANAGE_2_INSTANCE_ID=$(cat vmanage_2_instance_id)
aws ec2-instance-connect send-serial-console-ssh-public-key --instance-id $VMANAGE_2_INSTANCE_ID --serial-port 0 --ssh-public-key file://ed25519.pub --region $REGION
#vmanage_3
echo "vmanage_3"
vault kv get --field=vmanage_3_instance_id concourse/sdwan/$NAME/vmanage_3/vmanage_3_instance_id >> vmanage_3_instance_id
export VMANAGE_3_INSTANCE_ID=$(cat vmanage_3_instance_id)
echo $VMANAGE_3_INSTANCE_ID
#vbond_1
echo "vbond_1"
vault kv get --field=vbond_1_instance_id concourse/sdwan/$NAME/vbond_1/vbond_1_instance_id >> vbond_1_instance_id
export VBOND_1_INSTANCE_ID=$(cat vbond_1_instance_id)
aws ec2-instance-connect send-serial-console-ssh-public-key --instance-id $VBOND_1_INSTANCE_ID --serial-port 0 --ssh-public-key file://ed25519.pub --region $REGION
echo $VBOND_1_INSTANCE_ID
#vbond_2
echo "vbond_2"
vault kv get --field=vbond_2_instance_id concourse/sdwan/$NAME/vbond_2/vbond_2_instance_id >> vbond_2_instance_id
export VBOND_2_INSTANCE_ID=$(cat vbond_2_instance_id)
echo $VBOND_2_INSTANCE_ID
aws ec2-instance-connect send-serial-console-ssh-public-key --instance-id $VBOND_2_INSTANCE_ID --serial-port 0 --ssh-public-key file://ed25519.pub --region $REGION
#vsmart_1
vault kv get --field=vsmart_1_instance_id concourse/sdwan/$NAME/vsmart_1/vsmart_1_instance_id >> vsmart_1_instance_id
export VSMART_1_INSTANCE_ID=$(cat vsmart_1_instance_id)
aws ec2-instance-connect send-serial-console-ssh-public-key --instance-id $VSMART_1_INSTANCE_ID --serial-port 0 --ssh-public-key file://ed25519.pub --region $REGION
echo $VSMART_1_INSTANCE_ID
#vsmart_2
vault kv get --field=vsmart_2_instance_id concourse/sdwan/$NAME/vsmart_2/vsmart_2_instance_id >> vsmart_2_instance_id
export VSMART_2_INSTANCE_ID=$(cat vsmart_2_instance_id)
aws ec2-instance-connect send-serial-console-ssh-public-key --instance-id $VSMART_2_INSTANCE_ID --serial-port 0 --ssh-public-key file://ed25519.pub --region $REGION
echo $VSMART_2_INSTANCE_ID
#vedge
vault kv get --field=vedge_1_instance_id concourse/sdwan/$NAME/vedge_1/vedge_1_instance_id >> vedge_1_instance_id
export VEDGE_1_INSTANCE_ID=$(cat vedge_1_instance_id)
aws ec2-instance-connect send-serial-console-ssh-public-key --instance-id $VEDGE_1_INSTANCE_ID --serial-port 0 --ssh-public-key file://ed25519.pub --region $REGION
echo $VEDGE_1_INSTANCE_ID


#step-2-get the list of instances from the vault





