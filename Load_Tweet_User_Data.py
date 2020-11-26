#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import csv
import sqlite3
import os
import json
import urllib.request

conn = sqlite3.connect('dsc450.db')
c = conn.cursor()
tweetdata ='http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment5.txt'
webFD = urllib.request.urlopen(tweetdata)
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
    CONTRIBUTORS            VARCHAR2(50),
    USER_ID                 NUMBER(30),
    CONSTRAINT TWEET_FK1 FOREIGN KEY ( USER_ID )
        REFERENCES USER (USER_ID)
);
"""
createusertbl = """
CREATE TABLE IF NOT EXISTS USER (
    ID                      VARCHAR2(20),
    NAME                    VARCHAR2(200),
    SCREEN_NAME             VARCHAR2(100),
    DESCRIPTION             VARCHAR2(200),
    FRIENDS_COUNT           NUMBER(30)
);
"""
c.execute('DROP TABLE IF EXISTS USER;')
c.execute(createusertbl)   # create the USER table

c.execute('DROP TABLE IF EXISTS TWEET;')
c.execute(createtweettbl)   # create the TWEET table

os.chdir("C:/Users/USER/Desktop/DSC/DSC_450 Database For Analytics/Assignment/Assignment_7")
tdict ={}
rec = 0
myfile = open('Module7_errors.txt','w')
translation = {39: None} 
cleandata = []
userdata = []
for alltweet in webFD:
    try:
        tweet = json.loads(alltweet.decode('utf8'))
        col1 = tweet['created_at']
        if tweet['created_at'] is None or tweet['created_at'] == "" or 'null' in tweet['created_at'].lower(): # check for null and blank values
            col1 = None
        col2 = tweet['id_str']
        if tweet['id_str'] is None or tweet['id_str'] == "" or 'null' in tweet['id_str'].lower(): # check for null and blank values
            col2 = None
        col3 = tweet['text']
        if tweet['text'] is None or tweet['text'] == "" or 'null' in tweet['text'].lower(): # check for null and blank values
            col3 = None
        col4 = tweet['source']
        if tweet['source'] is None or tweet['source'] == "" or 'null' in tweet['source'].lower(): # check for null and blank values
            col4 = None
        col5 = tweet['in_reply_to_user_id']
        if tweet['in_reply_to_user_id'] is None or tweet['in_reply_to_user_id'] == "": # check for null and blank values
            col5 = None
        col6 = tweet['in_reply_to_screen_name']
        if tweet['in_reply_to_screen_name'] is None or tweet['in_reply_to_screen_name'] == "": # check for null and blank values
            col6 = None
        col7 = tweet['in_reply_to_status_id']
        if tweet['in_reply_to_status_id'] is None or tweet['in_reply_to_status_id'] == "": # check for null and blank values
            col7 = None
        col8 = tweet['retweet_count']
        if tweet['retweet_count'] is None or tweet['retweet_count'] == "": # check for null and blank values
            col8 = None
        col9 = tweet['contributors']
        if tweet['contributors'] is None or tweet['contributors'] == "" or 'null' in tweet['contributors'].lower(): # check for null and blank values
            col9 = None
        col10 = tweet['user']['id']
        if tweet['user']['id'] is None or tweet['user']['id'] == "": # check for null and blank values
            col10 = None
        col11 = tweet['user']['name']
        if tweet['user']['name'] is None or tweet['user']['name'] == "" or 'null' in tweet['user']['name'].lower(): # check for null and blank values
            col11 = None
        col12 = tweet['user']['screen_name']
        if tweet['user']['screen_name'] is None or tweet['user']['screen_name'] == "" or 'null' in tweet['user']['screen_name'].lower(): # check for null and blank values
            col12 = None
        col13 = tweet['user']['description']
        if tweet['user']['description'] is None or tweet['user']['description'] == "" or 'null' in tweet['user']['description'].lower(): # check for null and blank values
            col13 = None
        col14 = tweet['user']['friends_count']
        if tweet['user']['friends_count'] is None or tweet['user']['friends_count'] == "": # check for null and blank values
            col14 = None
        cleandata.append([col1,col2,col3,col4,col5,col6,col7,col8,col9,col10])
        userdata.append([col10,col11,col12,col13,col14])
    except ValueError:
        rec = rec + 1
        myfile.write(str(alltweet) + "\n")

print('Total number of records in error:', rec,'\n')

c.executemany('INSERT  INTO USER VALUES (?, ?, ?, ?, ?)', userdata)

result = c.execute('SELECT COUNT(1) FROM USER') # count number of records
r = result.fetchall()
print('Total number of records in USER table:',r[0][0],'\n')

c.executemany('INSERT INTO TWEET VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', cleandata)

result = c.execute('SELECT COUNT(1) FROM TWEET') # count number of records
r = result.fetchall()
print('Total number of records in TWEET table:',r[0][0],'\n')

print('Examples from TWEET table')
result = c.execute('SELECT * FROM TWEET WHERE ID_STR in (468541694279819264,468541807559987201)') # count number of records
r = result.fetchall()
for i in r:
    print(*i, sep='\t')

print('\nExamples from USER table')
result = c.execute('SELECT * FROM USER WHERE ID in (1297356302,154693424)') # count number of records
r = result.fetchall()
for i in r:
    print(*i, sep='\t')

myfile.close()
conn.commit()   # finalize inserted data
conn.close()    # close the connection