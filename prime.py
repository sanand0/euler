import numpy

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]   # Ensure that this is initialised with at least 1 prime
prime_dict = dict.fromkeys(prime_list, 1)
lastn      = prime_list[-1]

def _isprime(n):
    ''' Raw check to see if n is prime. Assumes that prime_list is already populated '''
    isprime = n >= 2 and 1 or 0
    for prime in prime_list:                    # Check for factors with all primes
        if prime * prime > n: break             # ... up to sqrt(n)
        if not n % prime:
            isprime = 0
            break
    if isprime: prime_dict[n] = 1               # Maintain a dictionary for fast lookup
    return isprime

def _refresh(x):
    ''' Refreshes primes upto x '''
    global lastn
    while lastn <= x:                           # Keep working until we've got up to x
        lastn = lastn + 1                       # Check the next number
        if _isprime(lastn):
            prime_list.append(lastn)            # Maintain a list for sequential access

# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
# primesfrom2to()
def _refresh(n):
    """ Input n>=6, Returns a array of primes, 2 <= p <= n """
    global prime_list
    n = n + 1
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    prime_list = numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
    return prime_list

def prime(x):
    ''' Returns the xth prime '''
    global lastn
    while len(prime_list) <= x:                 # Keep working until we've got the xth prime
        lastn = lastn + 1                       # Check the next number
        if _isprime(lastn):
            prime_list.append(lastn)            # Maintain a list for sequential access
    return prime_list[x]

def isprime(x):
    ''' Returns 1 if x is prime, 0 if not. Uses a pre-computed dictionary '''
    if x > prime_list[-1]:
        _refresh(x)                             # Compute primes up to x (which is a bit wasteful)
    return prime_dict.get(x, 0)                 # Check if x is in the list

def factors(n):
    ''' Returns a prime factors of n as a list '''
    _refresh(n)
    x, xp, f = 0, prime_list[0], []
    while xp <= n:
        if not n % xp:
            f.append(xp)
            n = n / xp
        else:
            x = x + 1
            xp = prime_list[x]
    return f

def all_factors(n):
   ''' Returns all factors of n, including 1 and n '''
   f = factors(n)
   elts = sorted(set(f))
   numelts = len(elts)
   def gen_inner(i):
       if i >= numelts:
           yield 1
           return
       thiselt = elts[i]
       thismax = f.count(thiselt)
       powers = [1]
       for j in xrange(thismax):
           powers.append(powers[-1] * thiselt)
       for d in gen_inner(i+1):
           for prime_power in powers:
               yield prime_power * d
   for d in gen_inner(0):
       yield d

def num_factors(n):
    ''' Returns the number of factors of n, including 1 and n '''
    div = 1
    x = 0
    while n > 1:
        c = 1
        while not n % prime(x):
            c = c + 1
            n = n / prime(x)
        x = x + 1
        div = div * c
    return div


'''
Optimisation notes:
# Function access FAIRLY slower than Array access is SLIGHTLY slower than local variable access
# Generators are SLIGHTLY slower than returning a list
# Dictionary access takes ZERO time
'''
