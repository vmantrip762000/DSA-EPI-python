###############
# Date: 12-18-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Strings (Pg Numbers: 67 - 79) 
# Pages covered: 
###############

"""
Docstring for 6_1_int_to_str

Implement an integer to string conversion function, and a string to integer conversison function,
For example, if the input to the first function is the integer 314,it should retum the string "314" and
if the input to the second function is the string "314" it should return the integer 314.
Hint: Build the result one digit at a time.

"""
def int_to_string(x) :
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
        # Adds the negative sign back if is_negative
    return ('-'if is_negative else '') + ''.join(reversed(s))
        
import functools
import string
def string_to_int (s) :
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c), 
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)
    