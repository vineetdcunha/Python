#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import statistics
import os.path

def compute_stats(column_name):
    'Read the column field from a CSV file.'
    lst = []
    n = 0
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, '../data/avocado.csv')
    with open(path,'r')as f:
        header = f.readline() # Reading the first row from CSV file
        header_list = header.split(',') # Adding the column names to the list
        n = header_list.index(column_name)  # FInd the index of the column
        for row in f:
            try:
                vals ="".join(row.split(',')[n])
                lst.append(float(vals))       # Adding the elements to the list
            except:
                break
        return lst

def readAndComputeMean_SM(column_name):
    'Find the mean of column using in built statistics module.'
    try:
        main_lst = compute_stats(column_name) # Call function to read column from CSV file
        return statistics.mean(main_lst) # Using statistics function to calculate mean
    except:
        return False

def readAndComputeMean_HG(column_name):
    'Find the mean of column using own developed function.'
    num_count = 0
    sum_value = 0.0
    avg_calc = 0.0
    main_lst = []
    try:
        main_lst = compute_stats(column_name) # Extract the values of column from CSV file
        num_count = len(main_lst) # Count the number of elemenst in the list
        for i in main_lst:
            sum_value = sum_value + i # Adding all the values
        avg_calc = sum_value / num_count # Division of sum of all values with nummber of elements
        return avg_calc
    except:
        return False

def readAndComputeMean_MML(column_name):
    'Find the mean of column using own developed function and function being memoryless.'
    try:
        main_lst = readAndComputeMean_HG(column_name) # Call function to calculate mean using homegrown code
        return main_lst # Using statistics function to calculate median
    except:
        return False

def readAndComputeSD_SM(column_name):
    'Find the standard deviation of column using in built statistics module.'
    try:
        main_lst = compute_stats(column_name) # Call function to read column from CSV file
        return statistics.stdev(main_lst) # Using statistics function to calculate standard deviation
    except:
        return False

def readAndComputeSD_HG(column_name):
    'Find the standard deviation of column using own developed function.'
    mean = 0.0
    std_dev = 0.0
    std_deviation = 0.0
    n = 0
    try:
        main_lst = compute_stats(column_name) # Extract the values of column from CSV file
        n = len(main_lst) # Find the number of elements in the list
        mean = readAndComputeMean_HG(column_name) # Reusing the above homegrown function to retrieve a mean of the column
        for i in main_lst:
            std_dev = float(std_dev + ((i - mean) ** 2))  # Finding the difference of each row with the mean and adding up
        std_deviation = (std_dev / (n-1))  # Division of standard deviation and number of elements
        std_deviation = float(std_deviation ** 0.5 )
        return std_deviation
    except:
        return False

def readAndComputeSD_MML(column_name):
    'Find the statistics of column using own developed function and function being memoryless.'
    try:
        main_lst = readAndComputeSD_HG(column_name) # Call function to calculate standard devaition using homegrown code
        return main_lst # Using statistics function to calculate median
    except:
        return False

def readAndComputeMedian_SM(column_name):
    'Find the median of column using own developed function.'
    try:
        main_lst = compute_stats(column_name) # Call function to read column from CSV file
        return statistics.median(main_lst) # Using statistics function to calculate median
    except:
        return False


def readAndComputeMedian_HG(column_name):
    'Find the median of column using own developed function.'
    n = 0
    median1 = 0.0
    median2 = 0.0
    median = 0.0
    try:
        main_lst = compute_stats(column_name) # Extract the values of column from CSV file
        main_lst.sort() # Sorting the list in ascending rder
        n = len(main_lst) # Count the number of elements in the list
        if (n % 2 ==0): # Checking if there are even number of elements
            median1 = main_lst[n//2]
            median2 = main_lst[n//2 - 1]
            median = (median1 + median2)/2 # Calculating the average
        else:
            median = main_lst[n//2] # Retrieving the elements if the number of elements are odd
        return median
    except:
        return False

def readAndComputeMedian_MML(column_name):
    'Find the statistics of column using own developed function and function being memoryless.'
    try:
        main_lst = readAndComputeMedian_HG(column_name) # Call function to calculate median using homegrown code
        return main_lst # Using statistics function to calculate median
    except:
        return False
    
def test_code(col_name):
    mean_SM = readAndComputeMean_SM(col_name) # Trigger readAndComputeMean_SM function
    sd_SM = readAndComputeSD_SM(col_name) # Trigger readAndComputeSD_SM function
    median_SM = readAndComputeMedian_SM(col_name) # Trigger readAndComputeMedian_SM function
    mean_HG = readAndComputeMean_HG(col_name) # Trigger readAndComputeMean_HG function
    sd_HG = readAndComputeSD_HG(col_name) # Trigger readAndComputeSD_HG function
    median_HG = readAndComputeMedian_HG(col_name) # Trigger readAndComputeMedian_HG function
    mean_MML = readAndComputeMean_MML(col_name) # Trigger readAndComputeMean_MML function
    SD_MML = readAndComputeSD_MML(col_name) # Trigger readAndComputeSD_MML function
    median_MML = readAndComputeMedian_MML(col_name) # Trigger readAndComputeMedian_MML function
    try:
        if mean_SM is False or mean_HG is False or  mean_MML is False or sd_SM is False or sd_HG is False or SD_MML is False or median_SM is False or median_HG is False or median_MML is False:
            print('Incorrect column name or cannot calculate stats for this column.')
            return 10
        else:
            if (round(mean_SM,2) == round(mean_HG,2) and round(mean_HG,2) == round(mean_MML,2)):
                print('Mean matching across all three techniques')
                if (round(sd_SM,2) == round(sd_HG,2) and round(sd_HG,2) == round(SD_MML,2)):
                    print('Standard deviation matching across all three techniques')
                    if (round(median_SM,2) == round(median_HG,2) and round(median_HG,2) == round(median_MML,2)):
                        print('Median matching across all three techniques')
                        return True
                    else:
                        print('Median value not matching across all three techniques')
                        return False
                else:
                    print('Standard deviation value not matching across all three techniques')
                    return False
            else:
                print('Mean value not matching across all three techniques')
                return False
    except:
        return False
  
if __name__ == "__main__":
    print('Welcome to program to calculate statistics')
    print('The statistics can be calculated on the following columns: "AveragePrice" "Total Volume" "4046" "4225" "4770" "Total Bags" "Small Bags" "Large Bags" "XLarge Bags"')
    print('In case of any typo with the column name, the function would not return any result. \n')
    col_name = input('Please enter the column name to calculate mean using statistics module.\n')
    if test_code(col_name) is True:
        print('The mean, median and standard deviation for ',col_name,'column is matching using all three techniques.')
    elif test_code(col_name) is False:
        print('The mean, median and standard deviation for',col_name,'column is not matching for the above mentioned calculation.')
    print('\nGood Bye')