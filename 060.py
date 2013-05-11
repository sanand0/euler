''' The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime. '''

import prime

series = [3, 7, 109, 673]
prime._refresh(100000000)
for n in xrange(1, 1000000):
    p = prime.prime(n)
    if p in series: continue

    if n % 1000 == 0: print '...', p

    all_are_primes = False
    for s in series:
        if not prime.isprime(int(str(s) + str(p))):
            all_are_primes = False
            break
        if not prime.isprime(int(str(p) + str(s))):
            all_are_primes = False
            break

    if all_are_primes:
        print p, p + sum(series)
        break

