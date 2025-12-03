###############
# Date: 12-03-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Primitive Types (Pg Numbers: 23-35) 
# Pages covered: 27 - 28
###############


"""
the expression x & (x - 1) clears the lowest set bit in x, and x & ~(x - 1) extracts
the lowest set bit of x. Here are a few examples: 16&(16-1) = 0,11&(11-1)= 10,20&(20-1) = 16,
16 &~ (16 - 1) = 16, 11 &~ (11 - 1) = 1, and 20 &~ (20 - l) = 4, where 20 = (10100)

"""


"""
A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0 corresponding to the
least significant bit (LSB), and the bit at index 63 corresponding to the most significant bit (MSB).
Implement code that takes as input a 64-bit integer and swaps the bits at indices i and j.

Hint: When is the swap necessary?

"""

def swap_bits(x, i, j):
    # extract i-th and j-th bits and see if they differ
    if (x >> i) & 1 != (x >> j) & 1:
        # i-th and j-th bits differ. We will swap then by flipping their values
        # Select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 1
        # when x = 0, we can perforn the flip XOR.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

print(swap_bits(20, 1, 4))