def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger] .
    # top group: A[larger: ] .
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified elenent
    while equal < larger:
        # A[equal] is the incoming unclassified element,
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


# Example
arr1 = [7, 2 ,5, 9, -5, -8, 6, 9, 7]
dutch_flag_partition(6, arr1)
print(arr1)
# IMPORTANT Note: For the function below arr1 will be: [2, 5, -8, -5, 6, 9, 9, 7, 7]
dutch_flag_partition(3, arr1)
print(arr1)
