"""
Note: ACCELERATING BIT MANIPULATION
1. x&(X-1) is used to clear lowest set bit in x. i.e. : 16 & (16-1) = 0, 11 & (11-1)= 10, 20 & (20-l) = 16
2. x & -(x - 1) extracts the lowest set bit of x. i.e. : 16 & ~(16 - 1) = 16, 11 & ~(11 - 1) = 1, and 20 & ~(20 - l) = 4.

"""

"""
PROBLEM STATEMENT:

Implement code that takes as input a 64-bit integer and swaps the bits at indices i and j.
Note: bit swapping must be done for an 8-bit integer.

"""

#Brute force: Convert the integer to binary form store each digit of binary number in ana array and then swap.

#Optimized approach:
"""
1. using Bit acceleration extract i-th and j-th bit and see if they differ
2. If i-th and j-th bits differ we swap them using bit mask. Since x^1 = 0 when x = 1 and 1
3. # when x = 0, we can perforn the flip XOR
1 << i means "shift the number 1 left by i bits." similarly you must understand 1 << j

"""

def swap_bits(x, i, j):
    # Extract the i-tfi and j-th bjts, and see jf they differ.
    if (x >> i) & 1 != (x >> j) & 1:
    # i-th and j-th bits differ. We wi77 swap then by flipping their val.ues
    # Select the bits to flip with bit_nask. Since x^I = 0 when x = I and 1
    # when x = 0, we can perforn the flip X1R.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

# The time complexity is O(1), independent of the word size.