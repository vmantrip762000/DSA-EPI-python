# Primitive types - 37/432
"""
Trial question: Write a program to list out number of bits set to 1 in binary form of input integer

"""

def count_bits(n):
    num_bits = 0
    while n:
        num_bits += n&1
        n >>= 1# shift all bits of n to the right by 1 position
    return num_bits

#x = count_bits(8)
#print(x)

"""
Time complexity: O(n) where n is number of bits needed to represent the integer

"""

"""

Compute parity(1 if number of 1s are odd else parity is 0) of a word. Compute for very large 64 bit binary numbers

"""

#Brute force

def brute_parity(n):
    result = 0
    while n:
        result ^= n&1
        n >>= 1
    return result

y = brute_parity(10)
print(y)


#Logic to optimize: x&(x-1) gives x with it's lowest set bit erased
#simply explained: I will directly drop 1s in my binary representation one by one, starting from the right hand side 
# Note: '^' is the XOR operator
def optimize_parity(n):
    result = 0
    while n:
        result ^= 1
        n &= n-1

    return result

y = optimize_parity(10)
print(y)


#Pg 39