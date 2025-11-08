###############
# Date: 11-07-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 41 - 42
###############


"""

Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.

"""

RED, WHITE, BLUE = range(3)
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        # Look for a snaller element,
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # Second pass: group elements Larger than pivot.
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

"""

We need to improve the time complexity of above code.
Problem in above code: It observed that for every iteration to find an element smaller than pivot we begin from the start of array (index i)
Suggested improvement: To improve tirne complexity, we make a single pass and move all the elements less than the pivot
to the beginning. In the second pass we move the larger elements to the end. It is easy to perform each pass in a single iteration, 
moving out-of-place elements as soon as they are discovered.

"""

def dutch_flag_partition_improve1(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        # Look for a snaller element,
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    # Second pass: group elements Larger than pivot.
    larger = len(A) - 1
    for i in reversed(range(len(A))): 
        if A[i] < pivot:
            break
        if A[i] > pivot:            
        # Look for a Larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A.
            A[i], A[larger] = A[larger], A[i]
            larger -= 1   


# The time complexity is O(n) and the space complexity is O(1).