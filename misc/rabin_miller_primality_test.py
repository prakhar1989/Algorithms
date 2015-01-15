import sys
import random


def is_probable_prime(n, k=7):
    """use Rabin-Miller algorithm to return True (n is probably prime)
       or False (n is definitely composite)

       the parameter k defines the accuracy of the test.
       """
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    if n & 1 == 0:  # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d & 1 == 0:
            s, d = s + 1, d >> 1
        # Use random.randint(2, n-2) for very large numbers
        for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in xrange(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    return False  # composite if we reached end of this loop
        return True  # probably prime if reached end of outer loop

print is_probable_prime(7)
print is_probable_prime(5915587277)
print is_probable_prime(48112959837082048697)
print is_probable_prime(671998030559713968361666935769)
print is_probable_prime(2425967623052370772757633156976982469681)
print is_probable_prime(22953686867719691230002707821868552601124472329079)
