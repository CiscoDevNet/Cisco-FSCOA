#Steps to Prep 
=====
Update the docker image with the intersight python modules - crypto etc.
Create a separate image for Intersight - 

From the Lab Gen remove out my keys - 
Create a separate repo for my keys
After share and make public for Anuj
Also add a pipeline for 
Simplify and reduce number of readme files to one - there are a lot in all the different directories.
Add in a pipeline job - to deploy the supercar ami 
Copy the AppD scripts into repo
Add job for appD and to start the script to activate the java nodes.

# cisco-fso-labs
cisco-fso-lab


All Documentation for this lab is included in the Docs Folder. 

This lab is open source, and Cisco Partners and Customers may use this code to train their own employees or customers on the Cisco FSO APIS 
and incorporate this lab material into their own tech stacks to also provide a "automation startup kit" for their knowlege workers interested
in developing software to these APIs 

Coming Release - 

Adding in the udpated automation to load the TE Agents via user-data upon boot for improved performance
The existing TE install script requires TERM be enabled which is extremely slow 

Refactor Docker Images to have fewer layers and see where possible to replace with Alpine

Document AWS STS Auth config with Vault and automate (this is currently manual)