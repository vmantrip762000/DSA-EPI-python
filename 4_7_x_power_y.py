###############
# Date: 12-11-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Primitive Types (Pg Numbers: 23-35) 
# Pages covered: 31 - 32
###############

"""
Docstring for 4_7_x_power_y
Write a program that takes a double x and an integer y and returns x**y. You can ignore overflow and
underflow.
Hint: Explolit mathematical properties of exponentiation.

"""

def power (x , y) :
    result, power = 1.0, y
    if y < 0:
        power,x = -power, 1.0/x
    while power:
        if power & 1:
            result *= x
        x, power = x*x, power >> 1
    return result

#Time Complexitty: O(n)