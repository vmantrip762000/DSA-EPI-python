###############
# Date: 12-04-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Primitive Types (Pg Numbers: 23-35) 
# Pages covered: 29 - 31

"""
Docstring for 4_5_bitwise_x_multiply_y


Write a program that multiplies two nonnegative integers. The only operators you are allowed to
use are 
1. assignment, 
2. the bitwise operators ,>>, <<, |, &, ~, ^ and
3. equality checks and Boolean combinations thereof.

You may use loops and functions that you write yourself. These constraints imply, for example,
that you cannot use increment or decrement, or test if x < y.
Hint: Add using bitwise operations; multiply using shift-and-add.



"""

def multiply (x , y) :
    def add(a, b):
        running_sum, carryin, k, temp_a, temp_b = 0,0, 1, a, b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
        return running_sum | carryin
    running_sum = 0
    while x: # Examines each bit of x.
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

# Total time complexity is o(n^2)

