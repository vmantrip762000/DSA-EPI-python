###############
# Date: 12-22-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Strings (Pg Numbers: 67 - 79) 
# Pages covered: 
###############


"""
Docstring for 6_2_base_conversion

Write a program that performs base conversion. The input is a string, an integer b1, and another
integer b2. The string represents an integer in base b1. The output should be the string representing
the integer in base b2. Assume 2 < b1,b2 < 16. Use " N' to represent L0, "B" for 11,.. ., and "F" for
15. (For example, if the string is "615", h is 7 and bz is 13, then the result should be "1A7", since
6x72 +1x7 + 5 = 1x 132 +70xL3+7.)
"""

# Hint: What base can you easily convert to and from?
import string
import functools


def convert_base (num_as_string, b1, b2) :

    def construct_from_base (num_as_int, base) :
        return (' ' if num_as_int == 0 else
        construct_from_base(num_as_int // base, base) +
        string.hexdigits [num_as_int % base] .upper())
    
    is_negative = num_as_string[0]
    num_as_int = functools. reduce (
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative :], 0)# Converting from base b1 to base 10 integer
    return ('-'if is_negative else '') + ('0'if num_as_int == 0 else
    construct_from_base (num_as_int, b2) )
