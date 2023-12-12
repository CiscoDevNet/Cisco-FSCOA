REPO CONTACT: sconrod@cisco.com

Pipeline login command:
======
fly --target=aspades login --concourse-url=http://prod-ci.devops-ontap.com:8080 -n aspades --username=aspades --password=

Set-Pipeline command:
==========
fly -t prod-ci set-pipeline -c /Users/sconrod/dev/devops-ontap/sdwan/pipelines/sdwan-pipeline-python_v3.yml -p us-west-1a -l $params file





