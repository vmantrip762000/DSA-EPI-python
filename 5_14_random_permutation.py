###############
# Date: 12-02-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 56 - 57
###############




import random
def random_sampling (k, A) :
    for i in range(k):
        # cenerate a random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

def compute_random_permutation(n) :
    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation

print(compute_random_permutation(10))

#Time Complexity: O(n)