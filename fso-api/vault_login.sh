VAULT_ADDR='http://prod-vault.devops-ontap.com:8200'
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $VAULT_TOKEN