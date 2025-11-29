###############
# Date: 11-28-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 50 - 52
###############

"""
Given an array A of n elements and a permutation P, apply P to A.
Hint: Any permutation can be viewed as a set of cyclic permutations. For an element in a cycle, how would
you identify if it has been permuted?

"""
def apply_permutation(perm , A) :
    for i in range(len(A)):
    # Check if the element at index i has not been noved by checking if
    # perm[i] is non negative.
        next = i
        while perm[next] >= 0:

            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # Subtracts 7en(pern) fron an entry in pern to nake jt negative,
            # which indicates the corresponding move has been performed.
            perm[next] -= len(perm)
            next = temp
            # Restore perm.
    perm[:] = [a + len(perm) for a in perm]
    return A

# Time complexity: O(n)
# Space Complexity: O(1)

print(apply_permutation([3, 1, 2, 0], ['a', 'b', 'c', 'd']))

"""
If we cannot use the sign bit, we can allocate an array of n Booleans indicating whether the
element at index i has been processed. Alternatively, we can avoid using O(n) additional storage by
going from left-to-right and applying the cycle only if the current position is the leftmost position
in the cycle.

"""

def apply_permutation_bool(perm, A) :
    def cyclic_permutation (start , perm , A) :
        i, temp = start, A[start]
        while True:
            next_i = perm[i]
            next_temp = A[next_i]
            A[next_i] = temp
            i, temp = next_i , next_temp,
            if i == start:
                break
    for i in range(len(A)):
        # Traverses the cycle to see if i is the minimum element
        j = perm[i]
        while j != i:
            if j < i:
                break
            j = perm[j]
        else:
            cyclic_permutation(i, perm, A)
    return A

print(apply_permutation_bool([3, 1, 2, 0], ['a', 'b', 'c', 'd']))