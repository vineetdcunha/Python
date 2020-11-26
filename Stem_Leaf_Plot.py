#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import os.path
def stem_and_leaf(num_input):
    'Main function to plot stem and leaf graph'
    lst = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, '../data/StemAndLeaf'+str(num_input)+'.txt')
    with open(path,'r')as f:
            line = f.read().splitlines() # Reading the txt file
            for row in line:
                try:
                    lst.append(int(row))      # Adding the elements to the list
                except:
                    break
            lst.sort() # Sorting the list
            row = [] # Initializing a list
            n = 0 # Initializing variables
            num = 0
            check_lst = []
            check_stem = []
            min_num = 0
            max_num = 0
            for i in lst:
                stem = i // 10 # Extracting the last digit of a number
                leaf = i % 10 # Extracting the all other digits except last
                for j in row:
                    num = j[0] # Pulling the 0th element of list (Stem value)
                    check_lst.append(num)   # Creating a list for stem values
                if (stem) not in check_lst: # Checking if stem value is already present
                    row.append([]) # Creating a sub list
                    row[n].append(stem) # Appending the stem value to the list
                    row[n].extend('|') # Adding a pipe symbol
                    row[n].extend([leaf]) # Appending leaf value for the first element from the text file
                    n = n + 1 # Incrementing the value of n
                else:
                    row[n - 1].extend([leaf]) # Adding the number as leaf to the previous stem.
            
            for j in row: # Extract the first element of multidimensional list
                check_stem.append(j[0]) # Append the values to a list
                
            min_num = int(min(check_stem)) # Find the minimum stem value
            max_num = int(max(check_stem)) # Find the maximum stem value
            for k in range(min_num,max_num,1): # Loop starting from minimum value upto max
                if k not in check_stem: # Adding the numbers not available for stem
                    row.append([]) # Creating a sub list
                    row[n].append(k) # Appending the stem value to the list
                    row[n].extend('|')
                    n=n+1
            row = sorted(row, key=lambda x: x[0]) # Sorting the multidimensional list based on the first element
            
            for i in row: # Looping the row list and printing value with commas and quotes
                print (" ".join(map(str,i)))

if __name__ == "__main__":
    print('Welcome')
    print('This code will plot the stem and leaf graph based on your input')
    user_input = input('Press "Y" if you want to plot graph, any other value to exit. \n')
    if user_input.upper() == 'Y': # Check value of user input
        while user_input.upper() == 'Y': # Loop until user selects Y
            num_input = input('Enter 1 ,2 or 3 to select a file. \n')
            try:
                if int(num_input) <= 3 and int(num_input) >= 1:
                    stem_and_leaf(str(num_input))
                else:
                    print('Not a valid file.')
            except:
                print('Not a valid file.')
            user_input = input('Press "Y" to plot the graph again or use another file, any other value to exit. \n')
    print('Good bye')
    