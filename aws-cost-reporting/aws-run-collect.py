#!/usr/bin/env python
#aws-run-collect.py
import json, re, csv
import subprocess
from subprocess import call, check_output

outfile = 'aws-cost.raw.json'


cmd='aws ce get-cost-and-usage --time-period Start=2023-04-01,End=2023-04-30 --granularity MONTHLY --group-by Type=DIMENSION,Key=SERVICE Type=TAG,Key=Tenant --metrics "BlendedCost" "UnblendedCost" "UsageQuantity"'

output = check_output("{}".format(cmd), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

with open(outfile, 'w') as my_file:
    my_file.write(output)


