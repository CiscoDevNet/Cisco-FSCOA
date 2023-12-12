az login
======
az login -u sconrod@cisco.com 

az config set extension.use_dynamic_install=yes_without_prompt

az storage azcopy blob upload -c ltrapp3000 --account-name ltrapp3000 -s "viptela-vmanage-genericx86-64-resize.vhd" -d viptela-vmanage-genericx86-64-resize-3.vhd --destination-blob-type PageBlob
The command requires the extension storage-preview. Do you want to install it now? The command will continue to run after the extension is installed. (Y/n):

Try
-DestBlobType Page

az storage blob copy start --account-name ltrapp3000 --destination-blob viptela-vmanage-genericx86-64-resize-2.vhd --destination-container ltrapp3000 --destination-blob-type PageBlob --source-uri https://ltrapp3000.blob.core.windows.net/ltrapp3000/viptela-vmanage-genericx86-64.vhd --auth-mode login

Storage Blob under different Resource Group to avoid deletion
====================
rg = eastusstorage
container= ltrapp3000

create a resource group
=======
az group create --location eastus --name eastus-sdwan

create ssh key
============
az sshkey create --name "azure-ssh" --resource-group eastus-sdwan

rivate key is saved to "/Users/sconrod/.ssh/1685587909_862729".


chmod 600

Create Public Ips
===========
az network public-ip create --name vmanage1-pubip --resource-group eastus-sdwan --sku standard --tier Regional
vmanage1-pubip
az network public-ip create --name vmanage2-pubip --resource-group eastus-sdwan --sku standard --tier Regional
az network public-ip create --name vmanage3-pubip --resource-group eastus-sdwan --sku standard --tier Regional

Create security group
=============
export RESOURCE_GROUP_NAME=myResourceGroup
export LOCATION=eastus-sdwan
az group create --name $RESOURCE_GROUP_NAME --location $LOCATION

Open Ports on SG for a vm
======
az vm open-port --port 80 --resource-group $RESOURCE_GROUP_NAME --name $VM_NAME

Create Virtual Network
===========
#az network vnet create -g MyResourceGroup -n MyVnet --address-prefix 10.0.0.0/16 --subnet-name MySubnet --subnet-prefixes 10.0.0.0/24

az network vnet create --name eastus-vnet-sdwan --resource-group eastus-sdwan --address-prefix 10.0.0.0/16 --subnet-name vpn0 --subnet-prefixes 10.0.1.0/24

nsg name
==========
eastus-vnet-sdwan

Create a Network Security Group
==========
az network nsg create --name eastus-sdwan-nsg --resource-group eastus-sdwan --location eastus

ngs name
========
eastus-sdwan-nsg

Create Network Security Rule
=====
#az network nsg rule create -g MyResourceGroup --nsg-name MyNsg -n MyNsgRuleWithAsg --priority 500 --source-address-prefixes Internet --destination-port-ranges 80 8080 --destination-asgs Web --access Allow --protocol Tcp --description "Allow Internet to Web ASG on ports 80,8080."
az network nsg rule create -g MyResourceGreastus-sdwanoup --nsg-name XXXXXXX -n MyNsgRuleWithAsg --priority 500 --source-address-prefixes Internet --destination-port-ranges 80 8080 22 --destination-asgs Web --access Allow --protocol Tcp --description "Allow Inbound from Inet."

#Create Custom Route Table or NAT GW
======================================

Add subnets to vnet
====================
az network vnet subnet create --resource-group eastus-sdwan --vnet-name eastus-vnet-sdwan --name vpn0 --address-prefixes 10.0.1.0/24 --network-security-group eastus-sdwan-nsg
az network vnet subnet create --resource-group eastus-sdwan --vnet-name eastus-vnet-sdwan --name vpn512 --address-prefixes 10.0.2.0/24 --network-security-group eastus-sdwan-nsg
az network vnet subnet create --resource-group eastus-sdwan --vnet-name eastus-vnet-sdwan --name cluster --address-prefixes 10.0.3.0/24 --network-security-group eastus-sdwan-nsg 

create nics
========

command returns:
"resourceGuid": "6e99e794-ed16-4cd5-8972-7098337abaec",

#vmanage1
az network nic create -g eastus-sdwan --vnet-name eastus-vnet-sdwan --subnet vpn0 --name vmanage1-vpn0 --network-security-group eastus-sdwan-nsg --public-ip-address vmanage1-pubip
az network nic create -g eastus-sdwan --vnet-name eastus-vnet-sdwan --subnet vpn512 --name vmanage1-vpn512 --network-security-group eastus-sdwan-nsg
az network nic create -g eastus-sdwan --vnet-name eastus-vnet-sdwan --subnet cluster --name vmanage1-cluster --network-security-group eastus-sdwan-nsg

#vmanage2
az network nic create -g eastus-sdwan --vnet-name eastus-vnet-sdwan --subnet vpn0 --name vmanage2-vpn0 --network-security-group eastus-sdwan-nsg --public-ip-address vmanage2-pubip
az network nic create -g eastus-sdwan --vnet-name eastus-vnet-sdwan --subnet vpn512 --name vmanage2-vpn512 --network-security-group eastus-sdwan-nsg
az network nic create -g eastus-sdwan --vnet-name eastus-vnet-sdwan --subnet cluster --name vmanage2-cluster --network-security-group eastus-sdwan-nsg

#vmanage3

az network nic create -g eastus-sdwan --vnet-name eastus-vnet-sdwan --subnet vpn0 --name vmanage3-vpn0 --network-security-group eastus-sdwan-nsg --public-ip-address vmanage3-pubip
az network nic create -g eastus-sdwan --vnet-name eastus-vnet-sdwan --subnet vpn512 --name vmanage3-vpn512 --network-security-group eastus-sdwan-nsg
az network nic create -g eastus-sdwan --vnet-name eastus-vnet-sdwan --subnet cluster --name vmanage3-cluster --network-security-group eastus-sdwan-nsg

create disk
============
az disk create --name vmanage1_disk --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus
vmanage1_disk

az disk create --name vmanage2_disk --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus
vmanage2_disk

az disk create --name vmanage3_disk --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus
vmanage3_disk


Create Virtual Machines
=================

export RG_NAME=eastus-sdwan
export LOCATION=eastus
export VM_NAME=vmanage1
export VM_IMAGE="/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/sdwan/providers/Microsoft.Compute/images/vmanage_20.11"
export ADMIN_USERNAME=cisco
export USERDATA=vmanage-user-data
export SIZE=Standard_F16s_v2
export SSH_KEY_NAME=azure-ssh
export USER_DATA="vmanage-user-data"
export VNET=sdwan
export SUBNET=vpn0
export NIC_VPN0="vmanage1-vpn0"



az vm create --resource-group $RG_NAME --name $VM_NAME --image $VM_IMAGE --specialized --admin-username $ADMIN_USERNAME --ssh-key-name --public-ip-sku Standard 
export $VM_IMAGE="/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/sdwan/providers/Microsoft.Compute/images/vmanage_20.11"

az vm create --resource-group RG_NAME --name $VM_NAME --image $VM_IMAGE --specialized --admin-username $ADMIN_USERNAME  --ssh-key-name $SSH_KEY_NAME --public-ip-sku Standard --user-data $USER_DATA - --nics $NIC_VPN0 --attach-os-disk --licence-type Other \
-l eastus --size $SIZE --vnet $VNET --subnet $SUBNET --data-disk-delete-option delete --public-ip-address --boot-diagnostics-storage ltrapp3000 

This works:
==============

#vmanage1
==========
az disk create --name vmanage1_disk --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus
vmanage1_disk

userdata=$(<vmanage-user-data)

az vm create --location eastus --resource-group eastus-sdwan --name vmanage1 --image vmanage01 --ssh-key-name azure-ssh --public-ip-sku Standard \
--size Standard_F16s_v2 --admin-username cisco --attach-data-disks vmanage1_disk --data-disk-delete-option delete --user-data $userdata --nics vmanage1-vpn0 vmanage1-vpn512 vmanage1-cluster --verbose --output json




#vmanage2
==========
az disk create --name vmanage2_disk --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus
vmanage2_disk

az vm create --location eastus --resource-group eastus-sdwan --name vmanage2 --image vmanage_20.11 --ssh-key-name azure-ssh --public-ip-sku Standard \
--size Standard_F16s_v2 --admin-username cisco --attach-data-disks vmanage2_disk --data-disk-delete-option delete --user-data $userdata --nics vmanage2-vpn0 vmanage2-vpn512 vmanage2-cluster --verbose --output json

#vmanage3
==========
az disk create --name vmanage3_disk --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus


az vm create --location eastus --resource-group eastus-sdwan --name vmanage3 --image vmanage_20.11 --ssh-key-name azure-ssh --public-ip-sku Standard \
--size Standard_F16s_v2 --admin-username cisco --attach-data-disks vmanage3_disk --data-disk-delete-option delete --user-data $userdata --nics vmanage3-vpn0 vmanage3-vpn512 vmanage3-cluster --verbose --output json



Trying...
=========
az vm create --location eastus --resource-group eastus-sdwan --name vmanage1 --image vmanage_20.11 --ssh-key-name azure-ssh --public-ip-address vmanage1-pubip \
--size Standard_F16s_v2 --admin-username azure-user --attach-data-disks vmanage1_disk --disk-controller-type NVMe --data-disk-delete-option delete --user-data vmanage-user-data --nics vmanage1-vpn0 --vnet eastus-vnet-sdwan --subnet vpn0 --verbose --output json 



Trying Create a VM from managed disk 
=====================
https://learn.microsoft.com/en-us/azure/virtual-machines/scripts/create-vm-from-managed-os-disks

1. Create a Managed Disk from the VHD
2. Create a data disk
3. Launch VM from the managed disk and attach the data disk

subscriptionId="ec680a4a-6717-4da9-949d-e320b2eebbc5"
osDiskName=-vmanage-1-test-2
diskSize=1024
storageType="Premium SSD LRS"
osType=linux
virtualMachineName=vmanage-test-02
snapshotId=
resourceGroupName=eastus-sdwan
managedDiskName=vmanage-1-test-2
managedDiskId="/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-1-test-2"

Trying 
========
userdata=$(<vmanage-user-data)

userdata=$(<aws_vmanage_user_data_sdc)

az vm create --name $virtualMachineName --resource-group $resourceGroupName --attach-os-disk "/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-1-test-2" --os-type $osType --public-ip-sku Standard"


This works but cannot login 
==================================
Create the Managed Disk from the blob first.
doing this in gui now.

Works but cannot login
=========================
az vm create --name vmanage-test-4 --resource-group $resourceGroupName --attach-os-disk "/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-1-test-4" \
--os-type $osType --public-ip-sku Standard  --user-data vmanage-user-data --ssh-key-name azure-ssh


userdata=$(<vmanage-user-data)

az vm create --name vmanage-test-5 --resource-group eastus-sdwan --attach-os-disk "/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-test-5" \
--os-type $osType --public-ip-sku Standard  --user-data $userdata --ssh-key-name azure-ssh 



az vm create --name vmanage-test-6 --resource-group eastus-sdwan --attach-os-disk "/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-test-6" \
--attach-data-disks vmanage-6-data --os-type $osType --public-ip-sku Standard  --user-data $userdata --ssh-key-name azure-ssh



az vm create --name vmanage-test-7 --resource-group eastus-sdwan --attach-os-disk "/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-7" \
--attach-data-disks vmanage-7-data --os-type $osType --public-ip-sku Standard  --user-data $userdata --ssh-key-name azure-ssh

Create an OS Disk from a page blob
======
https://learn.microsoft.com/en-us/azure/virtual-machines/scripts/create-managed-disk-from-vhd
======================
vhdUri="https://ltrapp3000.blob.core.windows.net/ltrapp3000/viptela-vmanage-genericx86-64.vhd"
diskSize=1024
storageType=StandardSSD_LRS
os-type=linux
location=eastus
resourceGroupName=eastus-sdwan

**************************************************************
Create the OS Disk from the Snapshot or Blob
===================
az disk create --resource-group $resourceGroupName --name $diskName --sku $storageType --location $location --size-gb $diskSize --source $vhdUri  --os-type linux
az disk create --resource-group eastus-sdwan --name vmanage-1-os --sku StandardSSD_LRS --location eastus --size-gb 1024 --source "https://ltrapp3000.blob.core.windows.net/ltrapp3000/viptela-vmanage-genericx86-64.vhd" --os-type linux

Get the id of the os disk above
==========================
"/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-1-os"

Create another data disk 
===========================

az disk create --name vmanage-1-data --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus

Create the VM from the OS Disk and attach the data disk
======================================
Testing the userdata file that formats and mounts the disk (this actually may need to happen in reverse. May need to actually create the vm from a blank disk and then mount the managed disk)

az vm create --name vmanage-test-1 --resource-group eastus-sdwan --attach-os-disk "/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-1-os" \
--attach-data-disks vmanage-1-data --os-type Linux --public-ip-sku Standard  --user-data $userdata --ssh-key-name azure-ssh

****************************************


#Final
=======

vmanage-1
===========

Create managed os disk
===============
az disk create --resource-group eastus-sdwan --name vmanage-1-os --sku StandardSSD_LRS --location eastus --size-gb 1024 --source "https://ltrapp3000.blob.core.windows.net/ltrapp3000/viptela-vmanage-genericx86-64.vhd" --os-type linux
#Get the resource Id of the managed disk
managedDiskId=$(az disk show --name vmanage-1-os--resource-group $resourceGroupName --query "id" -o tsv)
az disk show --name vmanage-1-os --resource-group eastus-sdwan --query "id" -o tsv

Create data disk
===============
az disk create --name vmanage-1-data --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus

Put user data file to var or call from vault***
===============
userdata=$(<aws_vmanage_user_data_sdc)

Create VM using OS disk and Data Disk and mount the user data file
==============================

az vm create --name vmanage-1 --resource-group eastus-sdwan --attach-os-disk "/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-1-os" \
--attach-data-disks vmanage-1-data --os-type linux --size Standard_F16s_v2 --public-ip-sku Standard  --user-data $userdata --ssh-key-name azure-ssh --nics vmanage1-vpn0 vmanage1-vpn512 vmanage1-cluster --verbose --output json


vmanage-2
=========

Create managed os disk
===============
az disk create --resource-group eastus-sdwan --name vmanage-2-os --sku StandardSSD_LRS --location eastus --size-gb 1024 --source "https://ltrapp3000.blob.core.windows.net/ltrapp3000/viptela-vmanage-genericx86-64.vhd" --os-type linux
#Get the resource Id of the managed disk
id=$(az disk show --name vmanage-2-os--resource-group $resourceGroupName --query "id" -o tsv)
az disk show --name vmanage-2-os --resource-group eastus-sdwan --query "id" -o tsv

Create data disk
===============
az disk create --name vmanage-2-data --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus

Put user data file to var or call from vault***
===============
userdata=$(<azure_vmanage_user_data_sdc)

Create VM using OS disk and Data Disk and mount the user data file
==============================

az vm create --name vmanage-2 --resource-group eastus-sdwan --attach-os-disk "/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-2-os" \
--attach-data-disks vmanage-2-data --os-type linux --size Standard_F16s_v2 --public-ip-sku Standard  --user-data $userdata --ssh-key-name azure-ssh --nics vmanage2-vpn0 vmanage2-vpn512 vmanage2-cluster --verbose --output json

manage-3
=========

Create managed os disk
===============
az disk create --resource-group eastus-sdwan --name vmanage-3-os --sku StandardSSD_LRS --location eastus --size-gb 1024 --source "https://ltrapp3000.blob.core.windows.net/ltrapp3000/viptela-vmanage-genericx86-64.vhd" --os-type linux
#Get the resource Id of the managed disk
id=$(az disk show --name vmanage-3-os--resource-group $resourceGroupName --query "id" -o tsv)
az disk show --name vmanage-3-os --resource-group eastus-sdwan --query "id" -o tsv

Create data disk
===============
az disk create --name vmanage-3-data --resource-group eastus-sdwan --architecture x64 --os-type linux --size-gb 1024 --sku StandardSSD_LRS --location eastus

Put user data file to var or call from vault***
===============
userdata=$(<azure_vmanage_user_data_sdc)

Create VM using OS disk and Data Disk and mount the user data file
==============================

az vm create --name vmanage-3 --resource-group eastus-sdwan --attach-os-disk "/subscriptions/ec680a4a-6717-4da9-949d-e320b2eebbc5/resourceGroups/eastus-sdwan/providers/Microsoft.Compute/disks/vmanage-3-os" \
--attach-data-disks vmanage-3-data --os-type linux --size Standard_F16s_v2 --public-ip-sku Standard  --user-data $userdata --ssh-key-name azure-ssh --nics vmanage3-vpn0 vmanage3-vpn512 vmanage3-cluster --verbose --output json

vbond
=======

vbond
====

Firewall Ports
=================
Ports
8443
UDP 5246
830
UDP 123456-13064
8444
UDP 0-65535
23456-24156
5247
443
22


Notes:
Created a Managed Disk from the VHD blob
Took Snapshot of disk 
Created a vm in the gallery from this snapshot
Created VM from the gallery image

try sending files to vmanage using netcat
netcat domain.com 4444 < original_file
https://www.digitalocean.com/community/tutorials/how-to-use-netcat-to-establish-and-test-tcp-and-udp-connections

