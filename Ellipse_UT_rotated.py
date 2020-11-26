#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."
import math
from problem_3_rotated import ellipse_overlap
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
    print('Angle of rotation: 10')
    check = main.get_input(1,1,2,1,10) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 2')
    print('Inputs: x,y,a,b = -1,-1,3,1.5')   
    print('Angle of rotation: 60')
    check = main.get_input(-1,-1,3,1.5,60) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 3')
    print('Inputs: x,y,a,b = -1,1,2,5')   
    print('Angle of rotation: -190')
    check = main.get_input(-1,1,2,5,-190) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 4')
    print('Inputs: x,y,a,b = -1,"one",2,5')   
    print('Angle of rotation: 0')
    check = main.get_input(-1,'one',2,5,0) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 5')
    print('Inputs: x,y,a,b = -1,1,0,5')   
    print('Angle of rotation: 70')
    check = main.get_input(-1,1,0,5,70) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nArea and circumference: Test Case 6')
    print('Inputs: x,y,a,b = -1,1,"one",5')
    print('Angle of rotation: 0')
    check = main.get_input(-1,1,'one',5,0) # calls function to validate input
    if check != False: # check if input is valid
        main.get_area() # get area
        main.get_circumference() # get circumference
    print ('\nOverlapping: Test Case 1')
    print('Inputs: x1,y1,a1,b1,theta1 = 0,0,3,2,0')
    print('Inputs: x2,y2,a2,b2,theta1 = 1,1,2.5,2,10\n')
    check = main.get_input_overlap(0,0,3,2,0,1,1,2.5,2,10) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap
    print ('\nOverlapping: Test Case 2')
    print('Inputs: x1,y1,a1,b1,theta1 = 1,1,2,1,100')
    print('Inputs: x2,y2,a2,b2,theta2 = 1,1,3,2,60\n')
    check = main.get_input_overlap(1,1,2,1,100,1,1,3,2,60) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap
    print ('\nOverlapping: Test Case 3')
    print('Inputs: x1,y1,a1,b1,theta1 = 1,1,4,2,30')
    print('Inputs: x2,y2,a2,b2,theta1 = -1,-1,3,2,50\n')
    check = main.get_input_overlap(1,1,4,2,30,-1,-1,3,2,50) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap
    print ('\nOverlapping: Test Case 4')
    print('Inputs: x1,y1,a1,b1,theta1 = 1,1,2,1,0')
    print('Inputs: x2,y2,a2,b2,theta2 = 1,1,2,1,0\n')
    check = main.get_input_overlap(1,1,2,1,0,1,1,2,1,0) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap()  # get overlap
    print ('\nOverlapping: Test Case 5')
    print('Inputs: x1,y1,a1,b1,theta1 = "one",-2,2,1,10')
    print('Inputs: x2,y2,a2,b2,theta2 = 1,1,3,2,10 \n')
    check = main.get_input_overlap('one',-2,2,1,10,1,1,3,2,10) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap
    print ('\nOverlapping: Test Case 6')
    print('Inputs: x1,y1,a1,b1,theta1 = 1,-2,0,1,0')
    print('Inputs: x2,y2,a2,b2,theta2 = 1,1,3,2,0')
    check = main.get_input_overlap(1,-2,0,1,0,1,1,3,2,0) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap
    print ('\nOverlapping: Test Case 7')
    print('Inputs: x1,y1,a1,b1,theta1 = 1,1,2,1,0')
    print('Inputs: x2,y2,a2,b2,theta2 = 1,1,3,2,0')
    check = main.get_input_overlap(1,1,2,1,0,1,1,3,2,0) # calls function to validate input
    if check != False: # check if input is valid
        main.get_overlap() # get overlap

    