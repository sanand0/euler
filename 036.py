'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

# Faster solution by AbsoluteZero
print sum(n for n in xrange(1, 1000000)
      if str(n)[::-1] == str(n) and bin(n)[2:] == bin(n)[-1:1:-1])

# My original solution
#
# def ispalindrome(n, base):
#     digits = []
#     reverse = []
#     while n > 0:
#         d = str(n % base)
#         digits.append(d)
#         reverse.insert(0, d)
#         n = n / base
#     return digits == reverse
#
# print sum(n for n in xrange(1, 1000000) if ispalindrome(n, 10) and ispalindrome(n, 2))

