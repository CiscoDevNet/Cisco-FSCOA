#aws-report-function.py
#Get List to Convert to CSV
import json
import csv
import pandas as pd
import re

report = 'aws-cost.raw.json'

with open(report) as access_json:
    read_content = json.load(access_json) #changing json into a python object using json encoder
    question_access = read_content['ResultsByTime']
    print(question_access)
    #print(type(question_access))
    #print(question_access[0]) #There is only one list item
    for question_data in question_access:
        #print(question_data)
        print(type(question_data))
    replies_access = question_data['Groups']
    #print(replies_access) #This is entire chunck
    print(type(replies_access))
    for replies_data in replies_access:
        print(replies_data) #By Service All Tenants
        #print(type(replies_data))
    for item in replies_data['Keys'], replies_data['Metrics']:
        #print(item) #This is the Goldy Gold! But only Prints Last ! Shows Service and Tenant Separate Line
        print(type(item))
    items = replies_data['Keys'], replies_data['Metrics'] #This is the Gold Here!
    #print(items)



        


#The input json file must have the generating command fixed in order to pass a list of tenant names or a wildcard
     
#def get_user_names():
#    question_access = read_content['ResultsByTime']
#    for question_data in question_access:
#        replies_access = question_data['Groups']
#        for replies_data in replies_access:
#            for item in replies_data['Keys'], replies_data['Metrics']:
#                items = replies_data['Keys'], replies_data['Metrics']
#                print(items)       
            
        

## Need to pass in all the names of all the tenants into the script array
##Strip out all the tenant names    
        
 #   user_name = replies_data['Keys']
 #   print(user_name)
 #   print(type(user_name))
        
        

    
 
