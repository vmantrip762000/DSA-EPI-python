###############
# Date: 12-01-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 52 - 54
###############

"""
Write a program that takes as input a permutation, and returns the next permutation under dictionary
ordering. If the permutation is the last permutation, return the empty array. For example, if
the input is (1,0,3,2) your function should retum <1,2,0,3>. If the input is (3,2,1,0), return O.
Hint: Study concrete examples.
"""

def next_permutation(perm):

    """
    The general algorithm for computing the next permutation is as follows:
    (1.) Find k such that p[k] < p[k + 1] and entries after index k appear in decreasing order.
    (2.) Find the smallest p[] such that p[] > p[k] (such an / must exist since pfkl < pfk + 1)).
    (3.) Swap p[] and p[k] (note that the sequence after position k remains in decreasing order).
    (4.) Reverse the sequence after position k.
    
    """
    inversion_point = len(perm) - 2
    while (inversion_point >= 0 and perm[inversion_point] > perm[inversion_point + 1]):
        inversion_point -= 1 #Inversion point was found to be number 2
    if inversion_point == -1:
        return [] 
    
    
    # perm is the last permutation
    # Swap the smallest entry after index inversion_point that is greater than
    # perm[inversion_point]. Since entries in perm are decreasing after
    # inversion_point , if we search in reverse order, the first entry that is
    # greater than perm[inversion_point] is the entry to swap with.

    # perm before loop is: [6,2,7,5,4,3,0]
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]: 
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point] # [6,3,7,5,4,2,0]
            break

    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:]) # [6, 3, 0, 2, 4, 5, 7]

    return perm

print(next_permutation([6,2,7,5,4,3,0]))

# Time Complexity : O(n)
# Space Complexity : O(1)
