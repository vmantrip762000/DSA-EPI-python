"""
Write a program which takes as input a sorted array and updates it so that all duplicates have been
removed and the remaining elements have been shifted left to fill the emptied indices. Return the
number of valid elements. Many languages have library functions for performing this operationyou
cannot use these functions.

"""

def delete_duplicates(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)-1):
        if A[write_index - 1] != A[i]:
            A[i] = A[i + 1]# We move just one element, rather than an entire subarray, and ensure that we move it just once.
            write_index += 1
    return write_index

my_Arr_count = delete_duplicates([2,3,5,5,7,7,7,11,17,13])
print(my_Arr_count)  #7