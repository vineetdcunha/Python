def validate_input(lst):
    'Validate the inputs for the square. The inputs should be entered in the order of x coordinate, y coordinates and width of the square.\n'
    print (validate_input.__doc__)
    n = len(lst) # Checks the number of elements
    for i in lst: # Loop thru the list
        try:
            int(i) # Verify if Int type
        except:
            return False
    if n == 3: # Check for number of elements
        return True
    else:
        return False

def validate_input_values(lst):
    'Validate the values of the inputs for the square.\n'
    print (validate_input_values.__doc__)
    n = len(lst) # Checks the number of elements
    for i in lst: # Loop thru the list
        try:
            int(i) # Verify if Int type
        except:
            return False
    if n == 3 and lst[n-1] > 0: # Check for number of elements and if width is positive
        return True
    else:
        print('Width of the square should be positive or the number of elements are less than 3.\n')
        return False

def calc_perimeter(lst):
    '\nValidate the values of the inputs for the square and calculate the perimeter.\n'
    print (calc_perimeter.__doc__)
    print('The input elements are entered in order of x coordinate, y coordinate and width of the square.')
    print('The value of X and Y coordinate can be positive or negative. Width of the square should be positive.\n')
    lst_val = lst
    n = len(lst) # Checks the number of elements
    if validate_input_values(lst_val) is True:
        return 'The perimeter of the square is ', 2*lst_val[n-1]*lst_val[n-1] # Returns the perimeter of the square
    else:
        print('Width of the square should be positive or the number of elements do not represent x coordinate, y coordinate and width of the square.\n')
        return -1

def calc_area(lst):
    '\nValidate the values of the inputs for the square and calculates the area.\n'
    print (calc_area.__doc__)
    print('The input elements are entered in order of x coordinate, y coordinate and width of the square.')
    print('The value of X and Y coordinate can be positive or negative. Width of the square should be positive.\n')
    lst_val = lst
    n = len(lst) # Checks the number of elements
    if validate_input_values(lst_val) is True:
        return 'The area of the square is ',lst[n-1]*lst[n-1] # Returns the area of the square
    else:
        print('Width of the square should be positive or the number of elements do not represent x coordinate, y coordinate and width of the square. \n')
        return -1

def overlap(lst1,lst2): # Function to accept two lists
    '\nCheck if the area of two squares are overlapping and return the common area.'
    print (overlap.__doc__)
    if validate_input_values(lst1) is True and validate_input_values(lst2) is True: # Check if width is valid
        if (lst2[0] >= lst1[0]) and (lst2[0] <= lst1[0] + lst1[2]):
        # x2 > x1  and x2 < x1 + w1
            if (lst2[1] >= lst1[1]) and (lst2[1] <= lst1[1] + lst1[2]):
            # y2 > y1 and y2 < y1 + w1
                area = ((lst1[0] + lst1[2]) - lst2[0]) * ((lst1[1] + lst1[2]) - lst2[1])
                # area = ((x1+w1) - x2) * ((y1+w1) - y2)
                return abs(area)
            elif (lst2[1] <= lst1[1]) and (lst1[1] <= lst2[1] + lst2[2]):
            # y2 < y1 and y1 < y2 + w2
                area = ((lst1[0] + lst1[2]) - lst2[0]) * ((lst2[1] + lst2[2]) - lst1[1])
                # area = ((x1+w1) - x2) * ((y2+w2) - y1)
                return abs(area)
        if (lst2[0] <= lst1[0]) and (lst1[0] <= lst2[0] + lst2[2]):
        # x2 < x1 and x1 < x2 + w2
            if (lst2[1] >= lst1[1]) and (lst2[1] <= lst1[1] + lst1[2]):
            # y2 > y1 and y2 < y1 + w1
                area = ((lst2[0] + lst2[2]) - lst1[0]) * ((lst1[1] + lst1[2]) - lst2[1])
                # area = ((x2+w2) - x1) * ((y1+w1) - y2)
                return abs(area)
            elif (lst2[1] <= lst1[1]) and (lst1[1] <= lst2[1] + lst2[2]):
            # y2 < y1 and y1 < y2 + w2
                area = ((lst2[0] + lst2[2]) - lst1[0]) * ((lst2[1] + lst2[2]) - lst1[1])
                # area = ((x2+w2) - x1) * ((y2+w2) - y1)
                return abs(area)
    else:
        return -1



if __name__ == "__main__":
    sq1 = [1,0,2] # Initiaize Variable
    sq2 = [2,1,5] # Initiaize Variable
    sq3 = [4,3,1] # Initiaize Variable
    sq4 = [1,5,3] # Initiaize Variable
    sq5 = [6,4,-3] # Initiaize Variable
    sq6 = [6,4,'three'] # Initiaize Variable
    print(validate_input(sq1)) # Trigger validate_input function. Validates the number of elements entered in the list.
    print(validate_input_values(sq2)) # Trigger validate_input_value function. Validates the values of elements entered in the list.
    print(calc_perimeter(sq4)) # Trigger calc_perimeter function. Validates the values of elements entered in the list and calculates the perimeter.
    print(calc_area(sq4)) # Trigger calc_perimeter function. Validates the values of elements entered in the list and calculates the area.
    print("The overlap of "+ str(sq1) + " and "+ str(sq2) + " is "+ str(overlap(sq1,sq2))) # Trigger the overlap function
    print("The overlap of "+ str(sq2) + " and "+ str(sq3) + " is "+ str(overlap(sq2,sq3))) # Trigger the overlap function
    print("The overlap of "+ str(sq2) + " and "+ str(sq4) + " is "+ str(overlap(sq2,sq4))) # Trigger the overlap function
    print("The overlap of "+ str(sq1) + " and "+ str(sq4) + " is "+ str(overlap(sq1,sq4))) # Trigger the overlap function
    print("The overlap of "+ str(sq1) + " and "+ str(sq5) + " is "+ str(overlap(sq1,sq5))) # Trigger the overlap function
    print("The overlap of "+ str(sq1) + " and "+ str(sq6) + " is "+ str(overlap(sq1,sq5))) # Trigger the overlap function
