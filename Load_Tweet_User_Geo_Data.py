#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import sqlite3
import os
import json
import time
import pandas as pd
import urllib.request
import numpy as np
import csv

def read_data(num,load_type):
  os.chdir("C:/Users/USER/Desktop/DSC/DSC_450 Database For Analytics/Final Exam")
  start_read = time.time()
  if load_type == 'F':
      tweetdata ='http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt'
      infile = urllib.request.urlopen(tweetdata)
      print('Start reading from url')
      data = open('tweet_data.json','w',encoding="utf8")
      print('Start writing to a file')
      for i in range(num):
          fd = infile.readline().decode("utf-8")
          #tweetdata = json.loads(fd)
          data.write(fd)
      data.close()
  end_read = time.time()
  print('Complete writing to a file')
  print(num ,'Tweet load - Total execution time to read from the url and write to the file:',str(end_read - start_read),'seconds \n')
  return (end_read - start_read)

def read_load_table(num,load_type):
  
  conn.execute('pragma journal_mode=wal')
  c = conn.cursor()
  os.chdir("C:/Users/USER/Desktop/DSC/DSC_450 Database For Analytics/Final Exam")
  start_rw = time.time()
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
    GEO_ID                  VARCHAR2(50),
    USER_NAME               VARCHAR2(200),
    CONSTRAINT TWEET_FK1 FOREIGN KEY ( USER_ID )
        REFERENCES USER (ID),
    CONSTRAINT TWEET_FK2 FOREIGN KEY ( GEO_ID )
        REFERENCES GEO (ID)
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
  creategeotbl = """
  CREATE TABLE IF NOT EXISTS GEO (
    ID                      VARCHAR2(50),
    LATITUDE                VARCHAR2(20),
    LONGITUDE               VARCHAR2(20)
  );
  """
  c.execute('DROP TABLE IF EXISTS USER;')
  c.execute(createusertbl)   # create the USER table
  
  c.execute('DROP TABLE IF EXISTS TWEET;')
  c.execute(createtweettbl)   # create the TWEET table

  c.execute('DROP TABLE IF EXISTS GEO;')
  c.execute(creategeotbl)   # create the GEO table
  
  rec = 0
  read_time = 0
  incr_cnt = 0
  none_cnt_n = 0
  none_cnt_y = 0
  cleandata = []
  userdata = []
  geodata = []
  userlatlong = []
  scatter_plot = []
  tweet_data = []

  myfile = open('Final_exam_errors.txt','w',encoding="utf8")
  if load_type == 'F':
    read_time = read_data(num,load_type)
    inputfile = open('tweet_data.json', 'r',encoding='utf-8')
  else:
    read_time = 0
    tweetdata ='http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt'
    inputfile = urllib.request.urlopen(tweetdata)

  for i in range(num):
    fd = inputfile.readline()
    if load_type == 'F':
      tweet = json.loads(fd)
    else:
      tweet = json.loads(fd.decode('utf8'))
    tweet_data.append(tweet)

  for tweet in tweet_data:
    if load_type == 'F':
      col11 = tweet['user']['name']
      if tweet['user']['name'] is None or tweet['user']['name'] == "" or 'null' in tweet['user']['name'].lower(): # check for null and blank values
        col11 = None
      if tweet['geo'] is None or tweet['geo'] == "": # check for null and blank values
        col16 = None
        col17 = None
        col18 = None
        col15 = None
      else:
        col16 = tweet['geo']['coordinates']
        col17 = str(col16[0])
        col18 = str(col16[1])
        col15 = str(col17 + col18)
      userlatlong.append([col11,col17,col18])
    else:
      try:
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
        col16 = tweet['geo']
        if tweet['geo'] is None or tweet['geo'] == "": # check for null and blank values
          col16 = None
          col17 = None
          col18 = None
          col15 = None
        else:
          col16 = tweet['geo']['coordinates']
          col17 = str(col16[0])
          col18 = str(col16[1])
          col15 = str(col17 + col18)
        c.execute('INSERT  INTO USER VALUES (?, ?, ?, ?, ?)', (col10,col11,col12,col13,col14))
        if tweet['geo'] is None or tweet['geo'] == "" and none_cnt_n == 0:
          result4 = c.execute('SELECT COUNT(1) FROM GEO WHERE ID IS NULL') # count number of records in TWEET table
          r4 = result4.fetchall()
          if r4[0][0] == 0:
            none_cnt_n = none_cnt_n + 1
            col15 = None
            c.execute('INSERT INTO GEO VALUES (?, ?, ?)', (col15,col17,col18))
        else:
          c.execute('INSERT INTO GEO VALUES (?, ?, ?)', (col15,col17,col18))
        c.execute('INSERT INTO TWEET VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col15,col11))
        conn.commit()
        cleandata.clear()
        userdata.clear()
        geodata.clear()
        incr_cnt = 0
        myfile.write(str(tweet) + "\n")
      except:
        rec = rec + 1
        myfile.write(str(tweet) + "\n")

  
  conn.commit()
  print(num ,' Tweet load - Total number of records in error:', rec,'\n')

  if load_type != 'F':
    print(num ,' Tweet load - Insert Table')
    result = c.execute('SELECT COUNT(1) FROM TWEET') # count number of records in TWEET table
    r = result.fetchall()
    print('Total number of records in TWEET table:',r[0][0])

    result1 = c.execute('SELECT COUNT(1) FROM USER') # count number of records in USER table
    r1 = result1.fetchall()
    print('Total number of records in USER table:',r1[0][0])

    result2 = c.execute('SELECT COUNT(1) FROM GEO') # count number of records in GEO table
    r2 = result2.fetchall()
    print('Total number of records in GEO table:',r2[0][0])

    conn.commit()
  
  end_rw = time.time()

  print(num ,' Tweet load - Total execution time to read from the url and insert into the table/file:',str((end_rw - start_rw)),'seconds \n')
  
  conn.commit()   # finalize inserted data
  #conn.close()    # close the connection
  if (load_type == 'F'):
    return userlatlong
  del cleandata
  del userdata
  del geodata
  del fd

  myfile.close()
  inputfile.close()

def query_count_username_min_lat_long():
  #start_cnt = time.time()
  result3 = c.execute('SELECT COUNT(1) FROM (SELECT U.NAME, MIN(G.LATITUDE), MIN(LONGITUDE) FROM TWEET T, USER U, GEO G WHERE G.ID = T.GEO_ID AND U.ID = T.USER_ID AND T.USER_NAME = U.NAME AND G.LATITUDE NOT NULL AND G.LONGITUDE NOT NULL AND T.USER_NAME NOT NULL GROUP BY U.NAME)')
  r3 = result3.fetchall()
  #print('Count of number of unique user name with minimum latitude and longitude: ',r3[0][0],'\n')
  return r3[0][0]
  #print('Total execution time to find the number of users:',str((time.time() - start_cnt)),'seconds \n')

def query_lat_long(presult):
  result3 = c.execute('SELECT U.NAME, MIN(G.LATITUDE), MIN(LONGITUDE) FROM TWEET T, USER U, GEO G WHERE  G.ID = T.GEO_ID AND U.ID = T.USER_ID AND T.USER_NAME = U.NAME AND G.LATITUDE NOT NULL AND G.LONGITUDE NOT NULL AND T.USER_NAME NOT NULL  GROUP BY U.NAME')
  r3 = result3.fetchall()
  if presult == 'Y':
    user_geo_output = open('user_sql_output.csv','w')
    headers = [i[0] for i in result3.description]
    csvFile = csv.writer(user_geo_output, delimiter=',', lineterminator='\r\n')
    csvFile.writerow(headers)
    csvFile.writerows(r3)
    user_geo_output.close()

def agg_file(lst):
  #data = open('test.txt','w',encoding="utf8")
  df = pd.DataFrame(lst,columns=['user_name','lat','long'])
  df["lat"] = pd.to_numeric(df["lat"])
  df["long"] = pd.to_numeric(df["long"])
  df = df.dropna(subset=['lat','long'])
  dfc = df.groupby('user_name', as_index=False)['lat','long'].min()
  dfc.to_csv('user_py_output.txt', index=False)
  return (dfc.shape[0])

if __name__ == "__main__":
  conn = sqlite3.connect((":memory:"), isolation_level=None)
  c = conn.cursor()
  lst = []
  r1 = 0
  r2 = 0
  lst = read_load_table(500000,'F') # input pased to read from url and load into list for python problem
  start_py = time.time()
  r1 = agg_file(lst) # process will convert the list into dataframe and group by to search
  print('Count of number of unique user name with minimum latitude and longitude (via file python): ',r1,'\n')
  print('Total execution time to find the number of unique user name with minimum latitude and longitude (via file python):',str((time.time() - start_py)),'seconds \n')
  read_load_table(500000,'N') # input pased to read from url and load to table
  start_sql = time.time()
  r2 = query_count_username_min_lat_long() # returns the count of records from SQL query
  print('Count of number of unique user name with minimum latitude and longitude (via SQL): ',r2,'\n')
  print('Total execution time to find the number of unique user name with minimum latitude and longitude (via SQL):',str((time.time() - start_sql)),'seconds \n')
  query_lat_long('Y') # Required to output results in txt format
  start_py = time.time()
  for i in range(10): # Run the py process 10 times
    r1 = agg_file(lst)
  print('10 time run - Total execution time to find the number of unique user name with minimum latitude and longitude (via file python):',str((time.time() - start_py)),'seconds \n')
  start_py = time.time()
  for i in range(100): # Run the py process 100 times
    r1 = agg_file(lst)
  print('100 time run - Total execution time to find the number of unique user name with minimum latitude and longitude (via file python):',str((time.time() - start_py)),'seconds \n')
  start_sql = time.time()
  for i in range(10):
    r2 = query_count_username_min_lat_long() # Run the SQL process 10 times
  print('10 time run - Total execution time to find the number of unique user name with minimum latitude and longitude (via SQL):',str((time.time() - start_py)),'seconds \n')
  start_sql = time.time()
  for i in range(100):
    r2 = query_count_username_min_lat_long() # Run the SQL process 100 times
  print('100 time run - Total execution time to find the number of unique user name with minimum latitude and longitude (via SQL):',str((time.time() - start_py)),'seconds \n')
  conn.close()