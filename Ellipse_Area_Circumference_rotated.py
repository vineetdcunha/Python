#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import math
class ellipse_default:
    'Creates a default ellipse class to set default parameters, find area and circumference'
    def __init__ (self,xcoord = 0,ycoord = 0, a = 0, b = 0, theta = 0):
        'Creates an ellipse with default parameters of (x,y) = (0,0) and (a,b) = (0,0)'
        self.x = (xcoord) # Sets value of x coordinate
        self.y = (ycoord) # Sets value of y coordinate
        self.major_axis = (a) # Sets value of major axis
        self.minor_axis = (b) # Sets value of minor axis
        self.theta = (theta) # Sets the value of rotation
        
         

    def get_area(self):
        'Returns area of an ellipse'
        print (ellipse_default.get_area.__doc__)
        area = 0.0
        print('This function will return the area of an ellipse.')
        area = math.pi * self.major_axis * self.minor_axis # calculates area
        print('Area of an ellipse: ',area,'\n')
    
    def get_circumference(self):
        'Returns circumference of an ellipse'
        print (ellipse_default.get_circumference.__doc__)
        circum = 0.0
        print('This function will return the circumference of an ellipse.')
        circum = 2 * math.pi * math.sqrt ((self.major_axis**2 + self.minor_axis**2)/2) # calculates circumference
        print('Circumference of an ellipse: ',circum,'\n')

