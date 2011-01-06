'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

import prime
from combinatorics import combinations

def cat(a,b):
    n, p = 0, 1
    while p <= b: n, p = n+1, 10*p
    return a * p + b

def concatenations_are_prime(primes):
    for pair in combinations(primes, 2):
        if not prime._isprime(cat(pair[0], pair[1])): return False
    return True

