#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import os
import pandas as pd
import numpy as np
import random

# Section a)
def generate_random_numbers(num_rec):
    df1 = np.random.randint(21,100,size=(num_rec))
    print("\nSection a)")
    print("\nArray of ",num_rec," numbers.")
    return df1

# Section b and c)
def validate_50_random_numbers():
    df2 = np.random.randint(low=1, high=100, size = 50)
    df3 = pd.Series(df2)
    df3 = df3[df3 < 33] 
    print("\nSection b)")
    print("\nNumber of elements having value less than 33.")
    print(df3.shape[0])
    df4 = np.reshape(df2, (5,10)) 
    print("\nOriginal array")
    print(df4)
    print("\nSection c)")
    print("\nReplace all elements of the said array with ((50 - 100)/100) which are greater than 50")
    df4[df4 >= 50] = (50 - 100)/50
    print(df4)

if __name__ == "__main__":
    try:
        x = int(input('Enter the number of records: \n'))
        while type(x) is int:
            if x > 0 and type(x) is int:
                output = generate_random_numbers(int(x))
                print(output)
                break
    except:
        print('Input should be a positive number.\n')
    validate_50_random_numbers()
