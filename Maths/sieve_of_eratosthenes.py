#Implementation of Sieve of Eratosthenes algorithm to generate all the primes upto N.

from math import sqrt,ceil

def sieve_of_eratosthenes(n):
    bool_array = [True] * (n+1)
    bool_array[0] = False
    bool_array[1] = False
    prime_array = []
    upper_bound = ceil(sqrt(n))
    for i in range(2,upper_bound):
        if bool_array[i] == True:
            for j in range(i*i,n+1,i):
                bool_array[j] = False
    for i in range(n+1):
        if bool_array[i] == True:
            prime_array.append(i)
    return prime_array

print(sieve_of_eratosthenes(50))
