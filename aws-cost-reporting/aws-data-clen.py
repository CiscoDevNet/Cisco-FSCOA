import json
import csv
import pandas as pd
import re
from datetime import date
today = date.today()
todaystr = today

#Clean the AWS raw data file
input = 'aws-report.raw.json'
output = 'aws-report.cln.csv'

#Characters I want to remove from the dirty data file
with open(input, 'r') as my_file:
    text = my_file.read()
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("}", "")
    text = text.replace("{", "")
    text = text.replace("$", ": ")
    text = text.replace("'", "")
    text = text.replace("<", "")
    text = text.replace(">", "")
    text = text.replace("class", "")
    text = text.replace("list", "")
    text = text.replace("dict", "")
    text = text.replace("Keys", "Service")
    text = text.replace(" Metrics: ", " ")
    text = text.replace("Amount:", "")
    text = text.replace("  ", "")
    text = text.replace("Unit: USD,", "")
    text = text.replace("Service:", "")
    text = text.replace("BlendedCost:", "")
    text = text.replace("UnblendedCost:", "")
    text = text.replace("UsageQuantity:", "")
    text = text.replace("Unit:", "")
    text = text.replace("  , ", "")
    text = text.replace("  ", " ")
    text = text.replace("Tenant: ,", " ,")
    text = text.replace("Tenant: ", "")
    text = text.replace(" N/A", "start_date, end_date, date, sp")


   

# If you wish to save the updates back into a cleaned up file
with open(output, 'w') as my_file:
    my_file.write(text)

#Delete the first line of the file
    
with open(output, 'r') as fin:
    data = fin.read().splitlines(True)
with open(output, 'w') as fout:
    fout.writelines(data[1:])

#Replace first line of data

    
with open(output) as f:
    lines = f.readlines()

lines # ['This is the first line.\n', 'This is the second line.\n']

lines[0] = "service, environment, tenant, unblendedCost, blendedCost, usageQuantity, start_date, end_date, date, sp\n"

lines # ["This is the line that's replaced.\n", 'This is the second line.\n']

with open(output, "w") as f:
    f.writelines(lines)
    print(lines)

    

