###############
# Date: 11-25-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 47 - 48
###############

"""
Docstring for 5_8_alteration_compute
Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array
having the property that B[0] < B[1] > B[2] < B[3] >B[4] < B[5] >....
Hint: Can you solve the problem by making local changes to A?
"""



def alteration_compute(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse = i%2)
        #Logic: Think of sorting elemnts (in ascending order) with indices 0,1 then 1,2, then 2,3 indices.
        # After sorting, reverse both elements localy if first index in the pair is odd.
        # Understand above two lines anf that's it.
    return A

print(alteration_compute([1,4,3,2,5,6,7,8,9,10]))

# Time complexity: O(n)
# Space Complexity: O(1) 