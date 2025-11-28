"""
A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.
Write a program that takes an integer argument and retums all the primes between 1 and that
integer. For example, if the input is 18, you should retum [2,3,5,7,77,13,17].
Hlnf; Exclude the multiples of primes.
"""

# Given n, retllrn all prines up to and incTuding n.
def generate_primes (n) :
    primes = []
    # is_prine[p] represents if p is prime or not. InitiaTTy, set each to
    # true, expecting 0 and 1. IIen use sieving to e-limjnate nonprines.
    
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2,n+1):
        if is_prime[p]:
            primes.append(p)
    # Sieve p's nu-ltiples.
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes

print(generate_primes(21))

# Time Complexity: O(n**(3/2)
# Space Complexity: O(n)

# I will improve above sieveing technique by startingsieveing only odd numbers from p^2 since all numbers between 0, p^2 were sieved earlier.
# Example take first 6 multiples of Multiples of  3 = 3, 6, 9, 12, 15, 18 and mutiples of 5 = 5, 10, 15, 20, 25, 30 . 
# So, here 15 is sieved twice in above process.

def generate_primes_new_sieve(n):
    if n < 2:
        return []
    # Purpose of creating size array is to track the odd numbers only!
    size = (n-3)//2 + 1 
    is_prime = [True]*size # odd-only Sieve of Eratosthenes: Odd numbers between 3 and n.
    primes = [2]
    for i in range(size):
        p = 2*i + 3 # number at index i in is_prime
        if is_prime[i]:#checks for True
            primes.append(p)
            # Convert p^2 to its index in the odd-only sieve:
            # index = (p*p - 3) // 2
        for j in range(2*i**2 + 6*i + 3, size, p):
            is_prime[j] = False
    return primes 

print(generate_primes(21))

# Time Complexity: O(n**(3/2) log(logn)**2)
# Space Complexity: O(n)