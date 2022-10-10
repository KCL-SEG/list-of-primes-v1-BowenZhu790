"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import numpy as np
def primes(number_of_primes):
    i = 1
    list = []
    while np.size(list) < number_of_primes:
        k = 1;
        if k != 1 and k != i and i % k == 0:
            list.append(i)
        i++
    return list
