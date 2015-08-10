"""

Implementation of Sieve of Eratosthenes algorithm to generate all the primes upto N.

Reference : https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Algorithm :
* We have a list of numbers from 1 to N.
* Initially, all the numbers are marked as primes.
* We go to every prime number in the list (<= N ^ 1/2) and mark all the multiples of this prime number which are bigger than the number itself as non-primes.

"""

from math import sqrt,ceil

def calculate_primes(n):
    bool_array = [True] * (n+1)
    bool_array[0] = False
    bool_array[1] = False
    upper_bound = ceil(sqrt(n))
    for i in range(2,upper_bound):
        if bool_array[i]:
            for j in range(i*i,n+1,i):
                bool_array[j] = False
    prime_array = [i for i in range(n+1) if bool_array[i]]
    return prime_array

if __name__ == "__main__":
    print(calculate_primes(50))
