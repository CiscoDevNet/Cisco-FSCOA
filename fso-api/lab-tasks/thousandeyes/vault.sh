!/bin/sh
export VAULT_ADDR="http://prod-vault.devops-ontap.com:8200"
vault login -method=aws header_value=prod-vault.devops-ontap.com role=vault
TE_GROUP=$(vault kv get -field=token concourse/cisco-fso-labs/te-group)