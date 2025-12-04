###############
# Date: 12-03-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Primitive Types (Pg Numbers: 23-35) 
# Pages covered: 28 - 29
###############

"""
Docstring for 4_4_closest_integer

Define the weight of a non negative integer x to be the number of bits that are set to 1 in its binary
representation. For example, since 92 in base-2 equals (1011100)2, the weight of 92 is 4.
Write a program which takes as input a nonnegative integer x and retums a number y which is not
equal to x, but has the same weight as x and their difference,|y - x|, is as small as possible. You can
assume x is not 0, or all 1s. For example, if x = 6, you should return 5. You can assume the integer
fits in 64 bits.

"""
def closest_int_same_bit_count(x):
    NUM_UNSIGNED_BITS = 64
    # the correct approach is to swap the two rightmost consecutive bits that differ.
    for i in range(NUM_UNSIGNED_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1)) # Swaps bit-i and bit-(i + 1)
            return x
    # Raise error if all bits of x are 0 or 1
    raise ValueError('All bits are 0 or 1')

# Time complexity is O(n), where n is the integer width.
# Time complexity is O(n), where n is the integer width.