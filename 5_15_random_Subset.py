###############
# Date: 12-03-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 57 - 58
###############


"""
Docstring for 5_15_random_Subset

Write a program that takes as input a positive integer n and a size k < n, and returns a size-k subset
of (0,1,2,. ..,n - 1). The subset should be represented as an array. All subsets should be equally
likely and, in addition, all permutations of elements of the array should be equally likely. You may
assume you have a function which takes as input a nonnegative integer t and retums an integer in
the set {0,1,.. .,t - 1} with uniform probability.

Note: 
The key to reducing the space complexity to O(k) is simulating A with a hash table.

"""
import random
def random_subset(n, k):
    changed_elements = {}
    for i in range(k):
        # GEnerate random index between i na d n-1 inclusive
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
    return [changed_elements[i] for i in range(k)]

# Time Complexity: O(k)
# Space Cmplexity: O(k)


