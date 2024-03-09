# Cisco-FSCOA
Cisco Full Stack Cloud Operations Automation

repo contact: sconrod@cisco.com, sherrilconrod@yahoo.com

Env Setup
If you do not have an existing CICD environment setup you can first set that up as follows:
1 Deploy KOPS kubernetes cluster to Cloud Provider & setup DNS with your domain
2. Deploy hashicorp vault helm chart, Configure Chart(update DNS etc in helm values)
3. Follow the steps at Concourse to setup the approle method of auth in vault and use the Cloud Provider docs to 
setup the CP with vault, for example, for AWS https://developer.hashicorp.com/vault/tutorials/cloud-ops/vault-auth-method-aws
4. Update Concourse Helm Values with approle and id ad well as DNS and deploy

Setup Group Access or AD/SSO or any SSO you like with Vault.
Deploy the pipeline
Verify the first pipeline with your custom params file (with your git ssh key) - this job checks that auth with all resources: git, dockerhub(public access),
cloud provider, vault etc. If green you can then instantiate your first pipeline run.![](../../../Desktop/Screenshot 2024-03-08 at 5.59.50 PM.png)