###############
# Date: 12-03-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Primitive Types (Pg Numbers: 23-35) 
# Pages covered: 24 - 26
###############

"""
How would you compute the parity of a very large number of 64-bit words?
Hint: Use a lookup table, but don't use 264 entries!

"""

"""
The brute-force algorithm iteratively tests the value of each bit while tracking the number
of 1s seen so far. Since we only care if the number of 1s is even or odd, we can store the number
mod 2
"""
def word_parity(x):
    parity = 0
    while x:
        parity ^= x&1
        x >>= 1
    return parity

print(word_parity(136)) #0
print(word_parity(11)) #1

# Time Complexity: O(n)

"""
Here is a great bit-fiddling trick
which you should commit to memory: x &(x - 1) equals x with its lowest set bit erased

Example: x&(x - 1) = (00101100) &(00101011) = (00101000)

"""

def word_parity_bit_manip(x):
    parity = 0
    while x:
        parity ^= 1
        x &= (x-1)
    return parity

print(word_parity_bit_manip(136)) #0
print(word_parity_bit_manip(11)) #1

# Time Complexity is O(k) where k is the numbe rof set bits in the input

"""

FINAL OPTIMIZATION: The XOR of a group of bits is its parity. We can exploit this fact to use
the CPU's word-level XOR instruction to process multiple bits at a time.
For example, the parity of (b63, b62,. .. ,b3,bz, b1, b0) equals the parity of the XOR of
(b63, b62,. . . ,b32) and (b31, b30,. .., b0). The XOR of these two 32-bit values can be computed with a
single shift and a shgle 32-bit XOR instruction. We repeat the same operation on 32-,16-,8-, 4-,
2-, and 1-bit operands to get the final result.

"""
def parity_half_xor(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    return x & 0x1

print(parity_half_xor(136)) #0
print(parity_half_xor(11)) #1

# Time Complexity: O(log(n))