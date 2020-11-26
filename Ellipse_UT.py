#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

from problem_3 import ellipse_overlap
class ellipse_main (ellipse_overlap):
    def print_intro(self):
        'Prints an introduction to the program'
        print ("This program simulates to find area of an ellipse, circumference of an ellipse")
        print ("and to find area of an overlap between two ellipse called '1' and '2'.")
        print ('The value of x and y coordinate can be positive or negative.')
        print ('The value of major axis and minor axis will always be positive.')



if __name__ == '__main__':
    main = ellipse_main() # creates object of the class
    main.print_intro() # calls intro
    print ('\nArea and circumference: Test Case 1')
    print('Inputs: x,y,a,b = 1,1,2,1')
    check = main.get_input(1,1,2,1) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 2')
    print('Inputs: x,y,a,b = -1,-1,3,1.5')
    check = main.get_input(-1,-1,3,1.5) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 3')
    print('Inputs: x,y,a,b = -1,1,2,5')
    check = main.get_input(-1,1,2,5) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 4')
    print('Inputs: x,y,a,b = -1,"one",2,5')
    check = main.get_input(-1,'one',2,5) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 5')
    print('Inputs: x,y,a,b = -1,1,0,5')
    check = main.get_input(-1,1,0,5) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 6')
    print('Inputs: x,y,a,b = -1,1,"one",5')
    check = main.get_input(-1,1,'one',5) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nOverlapping: Test Case 1')
    print('Inputs: x1,y1,a1,b1 = 0,0,3,2')
    print('Inputs: x2,y2,a2,b2 = 1,1,2.5,2\n')
    check = main.get_input_overlap(0,0,3,2,1,1,2.5,2) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap
    print ('\nOverlapping: Test Case 2')
    print('Inputs: x1,y1,a1,b1 = 1,1,2,1')
    print('Inputs: x2,y2,a2,b2 = 1,1,2,1\n')
    check = main.get_input_overlap(1,1,2,1,1,1,2,1) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap
    print ('\nOverlapping: Test Case 3')
    print('Inputs: x1,y1,a1,b1 = 1,1,4,2')
    print('Inputs: x2,y2,a2,b2 = -1,-1,3,2\n')
    check = main.get_input_overlap(1,1,4,2,-1,-1,3,2) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap
    print ('\nOverlapping: Test Case 4')
    print('Inputs: x1,y1,a1,b1 = -2,-2,2,1')
    print('Inputs: x2,y2,a2,b2 = 1,1,3,2\n')
    check = main.get_input_overlap(-2,-2,2,1,1,1,3,2) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap()  # get overlap
    print ('\nOverlapping: Test Case 5')
    print('Inputs: x1,y1,a1,b1 = "one",-2,2,1')
    print('Inputs: x2,y2,a2,b2 = 1,1,3,2 \n')
    check = main.get_input_overlap('one',-2,2,1,1,1,3,2) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap
    print ('\nOverlapping: Test Case 6')
    print('Inputs: x1,y1,a1,b1 = 1,1,2,1')
    print('Inputs: x2,y2,a2,b2 = 1,1,3,2')
    check = main.get_input_overlap(1,1,2,1,1,1,3,2) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap

    