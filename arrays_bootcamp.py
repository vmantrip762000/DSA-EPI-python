###############
# Date: 11-05-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 37-39
###############

"""
Array definition: Given an array A, A[i] denotes the (i + 1)th object stored in the
array. 

* Arrays in Python are provided by the list type. (The tuple type is an immutable list.) 

* A list is dynamically-resized, i.e., there's no limit to the number of values  that can be added to it or deleted or inserted 
at arbitrary locations.

Common array operations: 
* Retrieving/Reading and then updating A[i] takes O(1) time. Insertion into a full array can be handled by
resizing, i.e., allocating a new array with additional memory and copying over the entries from the original array.

* The time complexity to delete the element at index I from an array of length n is O(n - i).

"""



"""
Q1) Given that input is an array of integers, reorder its entries so that the even entries appear first.

"""

# Approach: 2 pointer idea is useful. next_even = 0, next_odd = len(arr) - 1.
# Now while next_even < next_odd. check if value at next_even is actually even. If not swap the odd and even and proceed. 
# At the end return the array

def even_elements_first(arr1):
    next_even, next_odd = 0, len(arr1) - 1
    while next_even < next_odd:
        if arr1[next_even] % 2 == 0:
            next_even += 1
        else:
            arr1[next_even], arr1[next_odd] = arr1[next_odd], arr1[next_even]
            next_odd -= 1
    return arr1


my_array = [7, 8, 3, 9, 2, 4, 5]
print(f'The original array is {my_array}')
even_elements_first(my_array)
print(f'The array with even elements first is {my_array}')

#Space complexity: O(1)
#Time Complexity: O(n)