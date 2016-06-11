######################################################################
# FILE: ex2b.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex2 2014-2015
# DESCRIPTION:
# A simple calculator asks the user for 2 numbers and a math operation
# and prints the the right answer
#######################################################################

#Asks the user to enter 2 numbers and a math operation
num1 = int(input("num1:"))
num2 = int(input("num2:"))
op = input("operation:")

if op != '+' and op != '-' and op != '*' and op != '/' and op != '%':
    #Check if the operation entered is illegal
    print("Unknown operator")
elif (op == '/' or op == '%') and num2 == 0:
    #Check if divide by 0
    print("Can't divide by 0")
elif op == '+':
    #Print the sum of the 2 numbers
    print(num1 + num2)
elif op == '-':
    #Print the difference of the 2 numbers
    print(num1 - num2)
elif op == '*':
    #Print the product of the 2 numbers
    print(num1 * num2)
elif op == '/':
    ##Prints the quotient of the 2 numbers
    print(num1 // num2)
else:
    ##Prints the modulo of the 2 numbers
    print(num1 % num2)
