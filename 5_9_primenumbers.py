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