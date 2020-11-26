#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import csv
import sqlite3
import os
import ast
import datetime as dt
import json

conn = sqlite3.connect('dsc450.db')
c = conn.cursor()
c.row_factory = sqlite3.Row
createtweettbl = """
CREATE TABLE IF NOT EXISTS TWEET (
    CREATED_AT              DATE,
    ID_STR                  VARCHAR2(20),
    TEXT                    VARCHAR2(200),
    SOURCE                  VARCHAR2(100),
    IN_REPLY_TO_USER_ID     NUMBER(30),
    IN_REPLY_TO_SCREEN_NAME VARCHAR2(50),
    IN_REPLY_TO_STATUS_ID   NUMBER(30),
    RETWEET_COUNT           NUMBER(30),
    CONTRIBUTORS            VARCHAR2(50)
);
"""
c.execute('DROP TABLE IF EXISTS TWEET;')
c.execute(createtweettbl)   # create the DRIVER_DTL table

os.chdir("C:/Users/USER/Desktop/DSC/DSC_450 Database For Analytics/Assignment/Assignment_5")
data ={}
fd = open('Assignment4.txt', 'r',encoding="utf8").read() # Read txt file
#data = fd.read().split('EndOfTweet')

data = [json.loads(str(item)) for item in fd.strip().split('EndOfTweet')]
cleandata = []
#print(data)

for sub in data:
    col1 = sub['created_at']
    if sub['created_at'] is None or sub['created_at'] == "" or 'null' in sub['created_at'].lower(): # check for null and blank values
        col1 = None
    col2 = sub['id_str']
    if sub['id_str'] is None or sub['id_str'] == "" or 'null' in sub['id_str'].lower(): # check for null and blank values
        col2 = None
    col3 = sub['text']
    if sub['text'] is None or sub['text'] == "" or 'null' in sub['text'].lower(): # check for null and blank values
        col3 = None
    col4 = sub['source']
    if sub['source'] is None or sub['source'] == "" or 'null' in sub['source'].lower(): # check for null and blank values
        col4 = None
    col5 = sub['in_reply_to_user_id']
    if sub['in_reply_to_user_id'] is None or sub['in_reply_to_user_id'] == "": # check for null and blank values
        col5 = None
    col6 = sub['in_reply_to_screen_name']
    if sub['in_reply_to_screen_name'] is None or sub['in_reply_to_screen_name'] == "": # check for null and blank values
        col6 = None
    col7 = sub['in_reply_to_status_id']
    if sub['in_reply_to_status_id'] is None or sub['in_reply_to_status_id'] == "": # check for null and blank values
        col7 = None
    col8 = sub['retweet_count']
    if sub['retweet_count'] is None or sub['retweet_count'] == "": # check for null and blank values
        col8 = None
    col9 = sub['contributors']
    if sub['contributors'] is None or sub['contributors'] == "" or 'null' in sub['contributors'].lower(): # check for null and blank values
        col9 = None
    cleandata.append([col1,col2,col3,col4,col5,col6,col7,col8,col9])# combine all columns together and insert in a list

c.executemany('INSERT INTO TWEET VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', cleandata)

result = c.execute('SELECT COUNT(1) FROM TWEET') # count number of records
r = result.fetchall()
print('Total number of records:',r[0][0])

result = c.execute('SELECT * FROM TWEET WHERE ID_STR in (397513618134024192,397513618100461568)') # count number of records
r = result.fetchall()
for i in r:
    print(*i, sep='\t')

conn.commit()   # finalize inserted data
conn.close()    # close the connection