###############
# Date: 12-10-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Primitive Types (Pg Numbers: 23-35) 
# Pages covered: 30 - 31
###############


"""
Docstring for 4_6_bitwise_x_divide_y

Given two positive integers, compute their quotient, using only the addition, subtraction, and
shifting operators.

Hint:Relate x/y to (x - y)/y.
"""


def divide (x , y) :
    result, power = 0, 32
    y_power = y<<power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
        result += 1 << power
        x -= y_power
    return result

# Time Complexity: O(n)