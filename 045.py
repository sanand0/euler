'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle        T_n=n(n+1)/2        1, 3, 6, 10, 15, ...
Pentagonal      P_n=n(3n-1)/2       1, 5, 12, 22, 35, ...
Hexagonal       H_n=n(2n-1)         1, 6, 15, 28, 45, ...

It can be verified that T_285 = P_165 = H_143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

MAX = 100000
triangle = [ n * (  n + 1) / 2 for n in xrange(0, MAX) ]
pentagon = [ n * (3*n - 1) / 2 for n in xrange(0, MAX) ]
hexagon  = [ n * (2*n - 1)     for n in xrange(0, MAX) ]
pentagon_dict = dict.fromkeys(pentagon, 1)
hexagon_dict  = dict.fromkeys(hexagon, 1)

for t in xrange(286, MAX):
    v = triangle[t]
    if pentagon_dict.has_key(v) and hexagon_dict.has_key(v):
        print v
        break