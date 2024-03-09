#This script will import the clean aws data to the database then run the sqlcommand to include the date range.

import pandas as pd
from sqlalchemy import create_engine

infile = 'aws-report.cln.csv'

# read CSV file
column_names = ['service','tenant','unblendedCost','blendedCost', 'usageQuantity', 'start_date', 'end_date', 'date', 'sp']

#df = pd.read_csv('2-6-20-aws-cln.csv', header = None, names = column_names)
#print(df)


engine = create_engine('mysql://root:mysql-fdqn.com/reporting')
#with engine.connect() as conn, conn.begin():
#    df.to_sql('awscost', conn, if_exists='append', index=False)



#df = pd.read_csv(infile,sep=',',quotechar='\'',encoding='utf8', error_bad_lines=False) # Replace Excel_file_name with your excel sheet name

df = pd.read_csv(infile, sep=',',quotechar='\'',encoding='utf8',error_bad_lines=False,names=['service','tenant', 'unblendedCost', 'blendedCost', 'usageQuantity', 'start_date', 'end_date', 'date', 'sp'], header=None)
df.to_sql('awscost',con=engine,index=False,if_exists='append') # Replace Table_name with your sql table name



'''
Add in a column that includes the created time and the modified time
Create a column that is the start_date end_date

ALTER TABLE awscosts
ADD COLUMN dates VARCHAR(15) AFTER sp;



 #start_date end_date and create-date and time

 
'''
