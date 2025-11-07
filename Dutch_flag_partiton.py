###############
# Date: 11-06-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 39-41
###############


"""

Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.

"""

RED, WHITE, BLUE = range(3)
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elernents smaller than pivot
    for i in range(len(A)):
        # Look for a snaller elernent,
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # Second pass: group elernents Larger than pivot.
    for i in reversed(range(len(A))): 
        if A[i] < pivot:
            break
        # Look for a Larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


#Space complexity: O(1)
#Time Complexity: O(n^2)