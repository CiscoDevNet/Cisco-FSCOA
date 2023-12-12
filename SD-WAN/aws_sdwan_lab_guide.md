aws lab guide
==============

open terminal in ide
cd to lab directory (you will have fun control on this directory)
git clone repo 
checkout branch (instructor will assign you a branch day of lab)
edit your lab_vars.py file to update the name of your lab (this is the same as your branch and will be provided to you by the instructor)
create a notes file in the directory and name it by your branch name ie)qhearts
git add -all
git commit -m "first commit"
git push

Now your git branch is ready to build your entire lab environment based off the name you specified in the lab_vars.py
in a multi-tenancy environment - you will have a separate git branch for every customer environment that is built from a value which may be their customerID

Every branch in the lab is a separate tenant in the multi-tenant environment we are building together
Imagine you are one Devops or Netops Team Member and everyone in the lab is also on your Team. 
Although we are updating the customerid manually, in your own company, you may chose to make an API call from the point of sale application 
after a financial transaction completes to purchase a tenancy on the SDWAN which would simply generate a new git branch, with the new vars.py file

Currently the pipeline is not set to automatically start building upon git push, because this is a lab, and people may make a mistake(likely). Therefore, 
we are allowing everyone to manually kick off the pipeline or manually trigger it when they are ready. This also gives the instructor time to discuss 
multi-tenancy topics. 

When the instructor prompts you, they will verify all branches have up to date lab_vars - you may start your pipeline.
The pipeline will deploy and name and tag all objects in the cloud provider with your customerid
vpc, subnets, route tables, internet gateway, security groups, instances from correct amis(these were created in advance as it is very time consuming as vmanage is created from a 20 GB VHD, assign elastic ips, add secondary volumes, create and attach secondary enis to the correct indexes
push an ed25519 key to the instances(so you can ssh to it later and poke around), place instances in the correct security groups, and configure each instance with the base required
sdwan configuration(the instructor will go over this in detail)

Once all pipelines are green (the instructor can see this, and it will take approximately 12 minutes)
We will discuss the manual steps to perform for multi-tenancy in regards to the root ca and certificate installation on the instances

Lets take a moment so you can logon to each instance and see what you have done so far in a familiar format via the cli
==========
open a separate terminal window for each instance type: vmanage, vbond, vsmart, vedge. 
in your pipeline, find the job "lab-env.md"
This job prints out the IP address of each of your instances along with the SSH key you can use to connect to the instances
This ed25519 ssh key is also in your vault, you can get it out of the vault (instructor will demonstrate, but it is outside the scope of this lab to have everyone do this yourself)
save the key into a directoy outside git
chmod 400 keyname
Now you can ssh to each instance in a separate tab
ssh -i keyname your instance ip
lets go ahead and also open the GUI for vmanage and change the password - there are a few things we must set in the gui (these are settings uncoupled from the API thus we must
set some things that we already have configured in the cli in the gui. This was a design plan by the sdwan team for which the meaning is unknown)

lets go ahead and change the password in the cli to match what we set in the gui
lets logout and log back in


We will run some manual cli commands(instructor will demonstrate)

send your vbond ip address to the lab instructor to update dns(the .1 address)

Now we will learn how to connect to the API to finish the job.
Since the API is new to many of you, instead of fully automating this in our pipeline, we are going to run an "automation task"
Instructor will demonstrate

We will then use the API to install the root CA using an automation task (the instructor will demo this)

We will then validate the traffic is working over the SDWAN using Thousand Eyes and you will logon to Thousand Eyes and we will do some analysis of the underlay and overlay networks.

At the end of the AWS lab we will stop all instances (as they are expensive)
Later at the end we may start them up and then add in one edge device from GCP and Azure.

We will repeat the above steps for each cloud provider and at the end we will compare the difference between cloud providers.

The nice part about this is you will see the beauty of how we can use nearly the same templates for SDWAN no matter the cloud provider (there are some slight difference)

We have now deployed SDWAN to three cloud providers entirely from code accept for several steps:
Creating and downloading the license serial file
Setting up our certificates for our multi-tenancy customers
Updating our lab_vars.py file (again, we are taking the place of what your point of sale app would do via api call)
creating the elastic IPs (I decided to do this as they are expensive and limited due to lab budget so I wanted to avoid a scenerio where a lab student would not over provision )
creating the DNS entries in S3(instructor will explain)






