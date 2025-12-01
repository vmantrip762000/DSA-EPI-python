###############
# Date: 12-01-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 54 - 55
###############


"""
Implement an algorithm that takes as input an array of distinct elements and a size, and returns
a subset of the given size of the array elements. All subsets should be equally likely. Return the
result in input array itself.
Hint: How would you construct a random subset of size k + 1 given a random subset of size k?

"""
import random
def random_sampling (k, A) :
    for i in range(k):
        # cenerate a random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
