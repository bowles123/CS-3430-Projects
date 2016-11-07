#Brian Bowles, Assignment 3, January 26, 2015.
import random
from math import exp

# Returns true if the given number is prime, false otherwise.
# num_trials defaulted to 50 because that seems to give me
# the most accurate answer.
def is_fermat_prime(num, num_trials = 50):
    if num == 1:
        return False
    
    trial, a = 1, random.randint(1, num - 1)

    while trial <= num_trials:
        if a**(num) % num == a % num and num % 2 != 0:
            return True;
        trial += 1
    return False;

# Finds all prime numbers in a give list.
def find_fermat_prime(lst):
    primes = []

    for i in range(len(lst)):
        if is_fermat_prime(lst[i])== True:
            primes.append(lst[i])
    return primes;

 # Generates a list of random numbers.   
def random_list(size, range_):
    list_, element = [], 0;

    while element < size:
        number = random.randint(1, range_)
        list_.append(number)
        element += 1
    return list_

