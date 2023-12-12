#https://learn.microsoft.com/en-us/cli/azure/image?view=azure-cli-latest
az image copy --source-object-name --source-resource-group --target-location --export-as-snapshot

#https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli
az login -u <username> -p <password>

#PS
$AzCred = Get-Credential -UserName <username>
az login -u $AzCred.UserName -p $AzCred.GetNetworkCredential().Password

Set up a Service Principal
https://learn.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli#4-sign-in-using-a-service-principal
az ad sp create-for-rbac 
Create a resource using a service principal

Azure Vault
https://developer.hashicorp.com/vault/docs/auth/azure
role assignments

Azure Concourse
https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fapplication-workloads%2Fconcourse%2Fconcourse-ci%2Fazuredeploy.json

https://learn.microsoft.com/en-us/cli/azure/storage/file?view=azure-cli-latest
Az Storage File

az copy
https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-blobs-upload

https://learn.microsoft.com/en-us/cli/azure/network/public-ip?view=azure-cli-latest
az network public create

https://learn.microsoft.com/en-us/cli/azure/network/nic?view=azure-cli-latest
az network nic create

https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-network-interface?tabs=azure-portal
Azure Network Interfaces


