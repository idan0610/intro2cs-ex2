######################################################################
# FILE: ex2a.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex2 2014-2015
# DESCRIPTION:
# The program asks the user to choose a shape and calculates its
# perimeter and area.
#######################################################################
import math #Import math module with usful math functions

#Ask the user to choose a shape for calculating (assume he enters a number)
#print("1: Rectangle, 2: Circle; 3: Triangle")
input_shape = int(input("Choose a shape:"))

#Check if the input number is correct (1, 2 or 3)
if input_shape != 1 and input_shape != 2 and input_shape != 3:
    #Not good! try again
    #print("You must choose an integer number between 1 to 3!")
    print("Please enter a valid number for shape: 1 for rectangle,\
 2 for circle, or 3 for triangle")
else:
    #Input is correct, continue the program
    if input_shape == 1:
        #User chose rectangle, asks width and height and calculate area and 
        #perimeter (assume he enters numbers)
        width = float(input("width:"))
        height = float(input("height:"))
        area = width*height
        perimeter = (2*width)+(2*height)
        
        #Prints the area and perimeter of the chosen shape
        print("area:", area)
        print("perimeter:", perimeter)
        
    elif input_shape == 2:
        #User chose circle, asks radius and calculate area and 
        #perimeter (assume he enters numbers)
        radius = float(input("radius:"))
        area = math.pi*math.pow(radius,2)
        perimeter = 2*math.pi*radius
        
        #Prints the area and perimeter of the chosen shape
        print("area:", area)
        print("perimeter:", perimeter)
        
    elif input_shape == 3:
        #User chose Triangle, asks 3 edges: a,b,c and calculate area and 
        #perimeter (assume he enters numbers)
        a = float(input("a:"))
        b = float(input("b:"))
        c = float(input("c:"))
        area = math.sqrt((a + b + c)*(a + b - c)*(b + c - a)*(c + a - b))
        area /= 4
        perimeter = a + b + c
            
        #Prints the area and perimeter of the chosen shape
        print("area:", area)
        print("perimeter:", perimeter)
