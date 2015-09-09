"""
Implementation of Sieve of Eratosthenes algorithm to generate all the primes upto N.

Algorithm :
 * We have a list of numbers from 1 to N.
 * Initially, all the numbers are marked as primes.
 * We go to every prime number in the list (<= N ^ 1/2) and mark all the multiples 
   of this prime number which are bigger than the number itself as non-primes.
"""

from math import sqrt,ceil

def generate_primes(n):
    bool_array = [False, False] + [True] * n              # start with all values as True, except 0 and 1
    for i in range(2, int(ceil(sqrt(n)))):                # only go to till square root of n
        if bool_array[i]:                                 # if the number is marked as prime
            for j in range(i*i,n+1,i):                    # iterate through all its multiples
                bool_array[j] = False                     # and mark them as False
    primes = [i for i in range(n+1) if bool_array[i]]     # return all numbers which are marked as True
    return primes
