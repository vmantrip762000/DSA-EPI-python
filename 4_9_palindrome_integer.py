###############
# Date: 12-17-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Primitive Types (Pg Numbers: 23-35) 
# Pages covered: 33 - 34
###############

"""
Docstring for 4_9_palindrome_integer

Write a Program that takes an integer and determines if that integer's representation as a decimal
string is a palindrome.
Hint: lt's easy to come up with a simple expression that extracts the least significant digit. Can you find a
simple expression for the most significant digit?
"""

import math

def is_palindrome_number(x):
    if x <= 0:
    
        return x == 0
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x * 10:
            return False
        x %= msd_mask # Renove the nost significant digit of x
        x //= 10 # Renove the least significant digix of x.
        msd_mask //= 100
    return True

# The time complexity is O(n), and the space complexity is O(1).