#Euclidean Calculator

#calculate the gcd of two numbers

from easygui import*
from math import*

#User Input
msg = "Calculate the gcd of: "
title = "Euclidean Calculator"
fieldnames = ["Number 1: ", "Number 2: "]
numbers = multenterbox(msg, title, fieldnames)

x_1 = 1
y_1 = 0

x_2 = 0
y_2 = 1

q = 0
num1 = int(numbers[0])
num2 = int(numbers[1])

if num1 < 0:
    num1 *= -1
elif num1 == 0:
    gcd = num2
if num2 < 0:
    num2 *= -1
elif num2 == 0:
    gcd = num1   

if num1 == num2:
    gcd = num1
elif num1 > num2:
    r_1 = num1
    r_2 = num2
else:
    r_1 = num2
    r_2 = num1

if (r_1 > 0) and (r_2 > 0):
    while r_2 != 0:
        #quotient value calculation
        q = floor(r_1 / r_2)
        
        #calculation of new x and y
        x_3 = (-q * x_2) + x_1
        y_3 = (-q * y_2) + y_1
        
        #x and y of diophantine eqn
        x_1 = x_2
        y_1 = y_2
        x_2 = x_3
        y_2 = y_3
        
        #remainders
        r_3 = r_1
        r_1 = r_2
        r_2 = r_3 - (q * r_1)
        
        gcd = r_1

print(gcd)

msg = "gcd ({}, {}) = {}".format (numbers[0], numbers[1], gcd)

msgbox(msg, "Euclidean Calculator", "Finish")
