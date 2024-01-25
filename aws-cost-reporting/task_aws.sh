#!/bin/sh
#!/usr/bin/env python
apt-get update
apt-get update python
apt install -y python3-pip
apt-get update
apt-get install -y awscli
apt-get install -y libmysqlclient-dev
export PATH=~/.local/bin:$PATH
pip3 install click
pip3 install pandas
pip3 install sqlalchemy
pip3 install mysqlclient
ls -la
export PATH=~/.local/bin:$PATH
ls -la
cd aws
cp -R .aws ~/
cp -R credentials ~/.aws
cp -R config ~/.aws
cat ./aws/credentials
python3 aws-run-collect.py
python3 aws-report-function.py > aws-report.cln.json
python3 aws-data-clen.py
sed -i 1,2d aws-report.cln.csv
#python3 aws-import-csv-good.py