#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import csv
import sqlite3
import os
import ast
import datetime as dt

conn = sqlite3.connect('dsc450.db')
c = conn.cursor()

createdrivertbl = """
CREATE TABLE IF NOT EXISTS DRIVER_DTL (
    LICENSE_NUMBER     NUMBER(20),
    RENEWED      VARCHAR2(10),
    STATUS   VARCHAR2(20),
    STATUS_DATE   DATE,
    DRIVER_TYPE VARCHAR2(20),
    LICENSE_TYPE VARCHAR2(20),
    ORIGINAL_ISSUE_DATE DATE,
    NAME VARCHAR2(100),
    SEX  VARCHAR2(8),
    CHAUFFEUR_CITY VARCHAR2(25),
    CHAUFFEUR_STATE VARCHAR2(5),
    RECORD_NUMBER VARCHAR2(20)
);
"""

c.execute('DROP TABLE IF EXISTS DRIVER_DTL;')
c.execute(createdrivertbl)   # create the DRIVER_DTL table

os.chdir("C:/Users/USER/Desktop/DSC/DSC_450 Database For Analytics/Assignment/Assignment_5")

fd = open('Public_Chauffeurs_Short_hw3.csv', 'r') # Read csv file
reader = csv.reader(fd)
next(reader) # skip header
data = list()
for row in reader:
    data.append(row) # loop thru the csv file and add data to the list
cleandata = list()
for i in data: # loop thru the list to clean and format the data
    col2 = i[1]
    if i[1] is None or i[1] == "" or 'null' in i[1].lower(): # check for null and blank values
        col2 = None
    else:
        col2 = col2.replace('-','/') # replace '-' with '/' to have a consistent format
    col4 = i[3]
    if i[3] is None or i[3] == "" or 'null' in i[3].lower(): # check for null and blank values
        col4 = 'None'
    else:
        col4 = col4.replace('/','-') # replace '-' with '/' to have a consistent format
        col4 = dt.datetime.strptime(str(col4),"%m-%d-%Y").date() # cast to date type
    col6 = i[5]
    if i[5] is None or i[5] == "" or 'null' in i[5].lower():
        col6 = 'None'
    col7 = i[6]
    if i[6] is None or i[6] == "" or 'null' in i[6].lower():
        col7 = 'None'
    else:
        col7 = col7.replace('/','-') # replace '-' with '/' to have a consistent format
        col7 = dt.datetime.strptime(str(col7),"%m-%d-%Y").date()  # cast to date type
    col1,col3,col5,col8,col9,col10,col11,col12 = i[0],i[2],i[4],i[7],i[8],i[9],i[10],i[11]
    cleandata.append([col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12])# combine all columns together and insert in a list
c.executemany('INSERT INTO DRIVER_DTL VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )', cleandata) # insert into table

result = c.execute('SELECT COUNT(1) FROM DRIVER_DTL') # count number of records
r = result.fetchall()
print('Total number of records:',r[0][0])

result2 = c.execute('SELECT COUNT(DISTINCT LICENSE_NUMBER) FROM DRIVER_DTL') # count number of distinct LICENSE_NUMBER
r2 = result2.fetchall()
print('Total distinct number of LICENSE_NUMBER:',r2[0][0])

result3 = c.execute('SELECT COUNT(1) FROM DRIVER_DTL WHERE RENEWED IS NULL') # count number of distinct LICENSE_NUMBER
r3 = result3.fetchall()
print('Total number of NULL RENEWED record:',r3[0][0])


fd.close()

conn.commit()   # finalize inserted data
conn.close()    # close the connection