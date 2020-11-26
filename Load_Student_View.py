#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import csv
import sqlite3
import os

conn = sqlite3.connect('dsc450.db')
c = conn.cursor()
createstudenttbl = """
CREATE TABLE IF NOT EXISTS STUDENT (
    STUDENTID   NUMBER(10),
    NAME        VARCHAR2(50),
    ADDRESS     VARCHAR2(100),
    GRADYEAR    NUMBER(4),
    CONSTRAINT STUDENT_PK PRIMARY KEY (STUDENTID)
);
"""
creategradetbl = """
CREATE TABLE IF NOT EXISTS GRADE (
    CNAME       VARCHAR2(100),
    STUDENTID   NUMBER(10),
    CGRADE      NUMBER(3,2),
    CONSTRAINT GRADE_FK FOREIGN KEY (CNAME)
        REFERENCES COURSE (CNAME),  
    CONSTRAINT GRADE_FK2 FOREIGN KEY (STUDENTID)
        REFERENCES STUDENT (STUDENTID)
);
"""
createcoursetbl = """
CREATE TABLE IF NOT EXISTS COURSE (
    CNAME        VARCHAR2(100),
    DEPARTMENT   VARCHAR2(10),
    CREDITS      NUMBER(10),
    CHAIR        VARCHAR2(25),
    CONSTRAINT COURSE_PK PRIMARY KEY (CNAME)
);
"""
createstudentdtlvw = """
CREATE VIEW IF NOT EXISTS STUDENT_DETAILS AS
    SELECT
        STU.STUDENTID,
        STU.NAME,
        STU.ADDRESS,
        STU.GRADYEAR,
        GR.CNAME,
        GR.CGRADE,
        CR.DEPARTMENT,
        CR.CREDITS,
        CR.CHAIR
    FROM
        STUDENT   STU,
        COURSE    CR,
        GRADE     GR
    WHERE
        STU.STUDENTID = GR.STUDENTID
        AND GR.CNAME = CR.CNAME;
"""

c.execute('DROP TABLE IF EXISTS STUDENT;')
c.execute(createstudenttbl)   # create the STUDENT table

c.execute('DROP TABLE IF EXISTS COURSE;')
c.execute(createcoursetbl)   # create the COURSE table

c.execute('DROP TABLE IF EXISTS GRADE;')
c.execute(creategradetbl)   # create the GRADE table

c.execute('DROP VIEW IF EXISTS STUDENT_DETAILS;')
c.execute(createstudentdtlvw)

os.chdir("C:/Users/USER/Desktop/DSC/DSC_450 Database For Analytics/Midterm")

file_data = [i.strip('\n').split(',') for i in open('student.txt')]
new_data = [[int(a), *b, int(d)] for a, *b, d in file_data] #convert string id to integer and float
c.executemany('INSERT INTO STUDENT VALUES (?, ?, ?, ?)', new_data)

file_data = [i.strip('\n').split(',') for i in open('course.txt')]
new_data = [[*a, int(c), d] for *a, c, d in file_data] #convert string id to integer and float
c.executemany('INSERT INTO COURSE VALUES (?, ?, ?, ?)', new_data)

file_data = [i.strip('\n').split(',') for i in open('grade.txt')]
new_data = [[a, int(b), float(c)] for a, b, c in file_data] #convert string id to integer and float
c.executemany('INSERT INTO GRADE VALUES (?, ?, ?)', new_data)

result = c.execute('SELECT * FROM STUDENT_DETAILS')

print('Section a)')
translation = {39: None} 
for row in result:
  row = str(row)[1:-1]
  print(row)

print('Fetching from view.')
result = c.execute('SELECT * FROM STUDENT_DETAILS')
translation = {39: None} 
myfile = open('student_details.txt','w')
for row in result:
  row = str(row)[1:-1]
  myfile.write(row.translate(translation) + "\n")

print('\n','Section c)')
print('Adding the below record to the file.')
print("8,  Elisa D Flores,  2548 Lakeshore Street California, 1994, Graphics,  3.5,  Data Science, 2,  Kevin Spacey",'\n')
myfile.write("8,  Elisa D Flores,  2548 Lakeshore Street California, 1994, Graphics,  3.5,  Data Science, 2,  Kevin Spacey")
myfile.close()

print('Section d)')
fd = open('student_details.txt', 'r') # Read csv file
reader = csv.reader(fd)
unique = []
dupes = []
data = []
for row in reader:
    col = row[4]+row[6]+row[7]
    if col.strip() not in data:
        data.append(col.strip())
for i in data:
    subject,dept = i.split(' ',1)
    rec = dept[:-2]
    if rec not in unique:
        unique.append(rec)
    else:
        dupes.append(rec)
if len(dupes) == 0:
    print('Functional dependencies not violated. Every Course Name is unique.')
else:
    print('Functional dependencies violated for the following course name. There are duplicate records for a combination of Credits and Course Name.')
    print(dupes[0])
fd.close()

print('\n','Section e)')
result = c.execute('SELECT DEPARTMENT,ROUND(AVG(CGRADE),2),COUNT(1) FROM STUDENT_DETAILS GROUP BY DEPARTMENT')
translation = {39: None} 
print('Department, Average Grade, Number of records')
for row in result:
  row = str(row)[1:-1]
  print(row.translate(translation))

file_data = [i.strip('\n').split(',') for i in open('student_details.txt')]
new_data = [[int(a),*b,int(d),e,float(f),g,int(h),i] for (a),*b,(d),e,(f),g,(h),i in file_data] 

cleandata = []
for row in new_data:
    col1 = row[5]
    col2 = row[6]
    cleandata.append([col2,float(col1)])

result = dict()

for k, v in cleandata:
    if k in result:
        result[k].append(v)
    else:
        result[k] = [v]

averages = []

for d in result:
    averages.append((d, sum(result[d]) / len(result[d]), len(result[d])))

translation = {39: None} 
print('\n','Section f)')
print('Department, Average Grade, Number of records')
for row in averages:
  row = str(row)[1:-1]
  print(row.translate(translation))

print('Note: Difference between the values from the txt file and SQL results (Data Science Department) is because of the extra record included in text file.')

conn.commit()
fd.close()

