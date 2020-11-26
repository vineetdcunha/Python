#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."
import os
import pandas as pd
import numpy as np
import random

os.chdir("C:/Users/USER/Desktop/DSC/DSC_450 Database For Analytics/Assignment/Assignment_8")

df=pd.read_csv("Employee.txt",names = ['FNAME', 'MNAME','LNAME','MOBILE','DOB','ADDRESS1','CITY','STATE','GENDER','SALARY','WORK','YEARS'])

print('\nCSV file data')
print(df)

# section a
result1 = df.loc[df['GENDER'] == 'M']
print('\nSection a)')
print('\nAll Male Employees')
print(result1)

# section b
result2 = df.loc[[df.loc[df['GENDER'] == 'F', 'SALARY'].idxmin()]]
print('\nSection b)')
print('\nLowest Salary for Female Employee')
print(result2)

# section c
result3 = df['SALARY'].groupby(df['MNAME'])
print('\nSection c)')
print('\nGrouping Salary by Middle Name')
for gname,gvalue in result3:
    print('Group Name: ',gname)
    print('Group Value: ')
    print(gvalue)
    print('-'*30)