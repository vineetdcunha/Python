#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

from problem_1 import ellipse_default
import random
import math
class ellipse_overlap (ellipse_default):
    'Creates an ellipse class to find the overlap'
    def get_input(self,xcoord,ycoord,a,b):
        'Creates an ellipse accepting user parameters of (x,y) and (a,b)'
        print (ellipse_overlap.get_input.__doc__) # Print docstring
        ellipse_default.__init__(self,xcoord,ycoord,a,b) # Call get_input default function
        if ((type(xcoord) is float or type(xcoord) is int) and  (type(ycoord) is float or type(ycoord) is int)):
            # Check if coordinates are integers 
            print('Coordinates of (x,y) = (',xcoord,',',ycoord,')')
            bool_check = True
        else:
            print('Invalid Coordinates.')
            bool_check = False
        if ((type(a) is float or type(a) is int ) and (type(b) is float or type(b) is int ) and a > 0 and b > 0)  and (bool_check == True) : # Check if the values of major and minor axis is positive and integers
            print('Length along x axis and length along y axis for an ellipse (a,b) = (',a,',',b,') \n')
            return (xcoord, ycoord,a,b)
        else:
            print ('Invalid inputs.')
            print ('Aborting request.')
            return False
    
    def get_input_overlap(self,x1,y1,a1,b1,x2,y2,a2,b2):
        'Creates two ellipses accepting user parameters of (x,y) and (a,b)'
        print (ellipse_overlap.get_input_overlap.__doc__) # Print docstring
        print('\nThe values for the first ellipse.')
        bool_check = ellipse_overlap.get_input(self,x1,y1,a1,b1) # Call get_input function for first ellipse
        if (bool_check != False): # Check if first input is valid
            print('\nThe values for the second ellipse.')
            bool_check = ellipse_overlap.get_input(self,x2,y2,a2,b2) # Call get_input function for second ellipse
        else:
            return False
        if (bool_check != False):
            self.h1 = x1 # Sets value of x coordinate for 1st ellipse
            self.k1 = y1 # Sets value of y coordinate for 1st ellipse
            self.a1 = a1 # Sets value of major axis for 1st ellipse
            self.b1 = b1 # Sets value of minor axis for 1st ellipse
            self.h2 = x2 # Sets value of x coordinate for 2nd ellipse
            self.k2 = y2 # Sets value of y coordinate for 2nd ellipse
            self.a2 = a2 # Sets value of major axis for 2nd ellipse
            self.b2 = b2 # Sets value of minor axis for 2nd ellipse
        else:
            return False

    def define_rect (self,x1,y1,x2,y2,a1,b1,a2,b2):
        'Defines the length of a rectangle around both the ellipses'
        print (ellipse_overlap.define_rect.__doc__) # Print docstring
        xmax = 0
        xmin = 0
        ymax = 0
        ymin = 0
        if ((x2 + (a2)) >= (x1 + (a1)) and (x2 - (a2)) <= (x1 + (a1)) and (x2 - (a2)) >= (x1 - (a1))):
        # if center and total of ellipse 2 > than ellipse 1 and within ellipse 1. Set the boundary of rectangle max to ellipse 2 and min to ellipse 1 (X axis)
            xmax = x2 + (a2)
            xmin = x1 - (a1)
        elif ((x2 + (a2)) >= (x1 + (a1)) and (x2 - (a2)) <= (x1 - (a1)) ):
        # if center and total of ellipse 2 > than ellipse and outside ellipse 1. Set the boundary of rectangle max to ellipse 2 and min to ellipse 2 (X axis)
            xmax = x2 + (a2)
            xmin = x2 - (a2)
        elif ((x1 + (a1)) >= (x2 + (a2)) and  (x1 - (a1)) <= (x2 + (a2)) and (x1 - (a1)) >= (x2 - (a2))):
        # if center and total of ellipse 1 > than ellipse and within ellipse 2. Set the boundary of rectangle max to ellipse 1 and min to ellipse 2 (X axis)
            xmax = x1 + (a1)
            xmin = x2 - (a2)
        elif ((x1 + (a1)) >= (x2 + (a2)) and  (x1 - (a1)) <= (x2 - (a2))):
        # if center and total of ellipse 1 > than ellipse and outside ellipse 2. Set the boundary of rectangle max to ellipse 1 and min to ellipse 1 (X axis)
            xmax = x1 + (a1)
            xmin = x1 - (a1)

        if ((y2 + (b2)) >= (y1 + (b1)) and (y2 - (b2)) <= (y1 + (b1)) and (y2 - (b2)) >= (y1 - (b1))):
        # if center and total of ellipse 2 > than ellipse 1 and within ellipse 1. Set the boundary of rectangle max to ellipse 2 and min to ellipse 1 (Y axis)
            ymax = y2 + (b2)
            ymin = y1 - (b1)
        elif ((y2 + (b2)) >= (y1 + (b1)) and (y2 - (b2)) <= (y1 - (b1)) ):
        # if center and total of ellipse 2 > than ellipse and outside ellipse 1. Set the boundary of rectangle max to ellipse 2 and min to ellipse 2 (Y axis)
            ymax = y2 + (b2)
            ymin = y2 - (b2)
        elif ((y1 + (b1)) >= (y2 + (b2)) and  (y1 - (b1)) <= (y2 + (b2)) and (y1 - (b1)) >= (y2 - (b2))):
        # if center and total of ellipse 1 > than ellipse and within ellipse 2. Set the boundary of rectangle max to ellipse 1 and min to ellipse 2 (Y axis)
            ymax = y1 + (b1)
            ymin = y2 - (b2)
        elif ((y1 + (b1)) >= (y2 + (b2)) and  (y1 - (b1)) <= (y2 - (b2))):
        # if center and total of ellipse 1 > than ellipse and outside ellipse 2. Set the boundary of rectangle max to ellipse 1 and min to ellipse 1 (Y axis)
            ymax = y1 + (b1)
            ymin = y1 - (b1)
        return xmin,ymin,xmax,ymax

    def plot_point_in_ellipse (self,x,y,h1,k1,h2,k2,a1,b1,a2,b2):
        'Finds if a point is inside an ellipse'
        e1 = float((((x - h1) ** 2) / a1 ** 2) + (((y - k1) ** 2) / b1 ** 2)) # checks if point is inside 1st ellipse
        e2 = float((((x - h2) ** 2) / a2 ** 2) + (((y - k2) ** 2) / b2 ** 2)) # checks if point is inside 2nd ellipse
        return e1,e2
    
    def get_overlap (self):
        'Finds the area between two overlapping ellipses'
        print (ellipse_overlap.get_overlap.__doc__)
        n = 10000
        print('The number of points simulated: ',n)
        overlap_ctr = 0
        outside = 0
        h1 = self.h1 # Sets value of x coordinate for 1st ellipse#
        k1 = self.k1 # Sets value of y coordinate for 1st ellipse
        h2 = self.h2 # Sets value of x coordinate for 2nd ellipse
        k2 = self.k2 # Sets value of x coordinate for 2nd ellipse
        a1 = self.a1 # Sets value of major axis for 1st ellipse
        b1 = self.b1 # Sets value of minor axis for 1st ellipse
        a2 = self.a2 # Sets value of major axis for 2nd ellipse
        b2 = self.b2 # Sets value of minor axis for 2nd ellipse
        xmin,ymin,xmax,ymax = ellipse_overlap.define_rect (self,h1,k1,h2,k2,a1,b1,a2,b2) # Call define_rect function to define the boundary of the rectangle
        print (ellipse_overlap.plot_point_in_ellipse.__doc__)
        for i in range(n):
            x = round(random.uniform(xmin,xmax),5) # Generate random x coordinate between xmin and xmax
            y = round(random.uniform(ymin,ymax),5) # Generate random y coordinate between xmin and xmax
            area1,area2 = ellipse_overlap.plot_point_in_ellipse (self,x,y,h1,k1,h2,k2,a1,b1,a2,b2) # check if point is inside an ellipse
            if area1 <= 1 and area2 <= 1: # check if the coordinates are inside both the ellipses
                overlap_ctr += 1 # increment the counter
            else:
                outside += 1
        if overlap_ctr == 0: # if the ellipses are not overlapping
            print('The two ellipses do not overlap.\n')
        else:
            rect_area =  (xmax - xmin) * (ymax - ymin) # calculate the area of rectangle
            overlap_area = rect_area * (overlap_ctr/n) # calculate the overlapping area based on the counter value
            print ('Area of two overlapping ellipse: ',overlap_area) # return the value of the area



