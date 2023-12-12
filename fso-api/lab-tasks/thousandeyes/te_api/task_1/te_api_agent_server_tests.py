#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
token = os.getenv('TE_OATHTOKEN')
url = "https://api.thousandeyes.com/v6/agents.json"
payload={}
headers = {'Authorization': 'Bearer ' + token}
agent_response = requests.request("GET", url, headers=headers, data=payload)
print(agent_response)

'''
This will first fail as the test already exists. Run it, let it fail
Change the test name and re-run, it will create a new test and add all the enterprise agents to the test
'''
test_name = 'sc-11-23-test-14'

agent_list_json = agent_response.json()
print("Printing Agent List Json")
print(agent_list_json)

agent_list = agent_list_json['agents']
list_of_dictionaries = agent_list
sought_value = "Enterprise"
found_values = []
for dictionary in list_of_dictionaries:
    if (dictionary["agentType"] == "Enterprise"):
        found_values.append(dictionary)
print(found_values)

empty_list=[]
for item in found_values:
    agentId=item['agentId']
    print(agentId)
    empty_list.append({'agentId': agentId})
print(empty_list)

#For some reason the API will only see to accept the list of agents like this.....
#The expected format of the list of agents, is cumbersome because it requires you to create a list of dictionaries instead of just using the list of agentIDs
#agents = [{'agentId': '443526'}, {'agentId': '443531'}]
url='https://api.thousandeyes.com/v6/tests/agent-to-server/new.json'
payload = {'interval': '300', 'agents': empty_list, 'testName': test_name, 'port': '80', 'server': 'www.thousandeyes.com','alertsEnabled': '0'}
header = {'content-type': 'application/json', 'authorization': 'Bearer ' + token}
r = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
print(r)

print("here is your Thousand Eyes Oathtoken in case you would like to use the jupyter notebook to look at the json payloads in more detail...")
print(token)