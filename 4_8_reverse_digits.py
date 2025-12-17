###############
# Date: 12-16-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Primitive Types (Pg Numbers: 23-35) 
# Pages covered: 32 - 33
###############



"""
Docstring for 4_8_reverse_digits

Write a program which takes an integer and returns the integer corresponding to the digits of the
input written in reverse order. For example, the reverse of 42 is 24, and the reverse of -314 is -413.

Hint: How would you solve the same problem if the input is presented as a string?

"""




def reverse_digits(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = (result*10) + (x_remaining%10)
        x_remaining //= 10
    return -result if x < 0 else result


# The time complexity is O(n), where n is the number of digits in k.

