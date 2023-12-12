fly --target=prod-ci login --concourse-url=http://prod-ci.devops-ontap.com:8080 -n main --username=ci --password=

fly -t sdwan set-pipeline -c sdwan-pipeline-python_v3.yml -p viptela-sdwan -l /Users/sconrod/dev/cisco-fso-lab-gen/params/sdwan-us-west-2/us-west-2a.yml