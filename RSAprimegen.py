# RSAprimegen.py
# This is a file for functions involved generating random primes
# including:

from os import urandom
import math
import RSAprecompute
import RSAhelp


#######################################################
### Prime generation ##################################
#######################################################

def retry_until_prime(low, high):
    """NAIVE: finds primes by picking numbers at random and checking"""
    p = 1
    prime = False
    print(p)
    while(not prime):
        print("start loop")
        p = crypto_rand(low,high)
        print(p)
        prime = miller_rabin(p)
        print("end loop. ", "prime" if prime else "not prime")
    return p


def wheel_find_prime(low,high,wheel_degree=0):
    """ Finds prime between low and high using prime wheel.
    Randomly selects values "multiple" and "offset" such that
    "candidate" = multiple * wheel_size + offset
    """
    assert(low<high)
    # for small primes, just pick randomly from predetermined primes.
    if(high < max(RSAprecompute.small_primes)):
        rand_ind = RSAhelp.crypto_rand(len(RSAprecompute.small_primes))
        return RSAprecompute.small_primes[rand_ind]

    candidate = 0
    if(wheel_degree):
        wheel_size = 1
        for i in range(wheel_degree+1):
            wheel_size = wheel_size*RSAprecompute.small_primes[i]
        wheel = prime_wheel(7)

        while(candidate<low or candidate>=high or
              not RSAhelp.miller_rabin(candidate)):

            multiple = RSAhelp.crypto_rand(math.floor(low/wheel_size),
                                   math.ceil(high/wheel_size))

            index_within_wheel = RSAhelp.crypto_rand(len(wheel))
            offset = wheel[index_within_wheel]
            candidate = multiple * wheel_size + offset

        
    
    else:
        wheel_degree = len(RSAprecompute.prime_wheels)-1
        wheel_size = RSAprecompute.primorials[wheel_degree]
        while(wheel_size > high-low):
            wheel_degree = wheel_degree - 1
            wheel_size = RSAprecompute.primorials[wheel_degree]


        while(candidate<low or candidate>=high or
              not RSAhelp.miller_rabin(candidate)):

            multiple = RSAhelp.crypto_rand(math.floor(low/wheel_size),
                                   math.ceil(high/wheel_size))

            index_within_wheel = RSAhelp.crypto_rand(
                len(RSAprecompute.prime_wheels[wheel_degree]))
            offset = RSAprecompute.prime_wheels[wheel_degree][index_within_wheel]

            candidate = multiple * wheel_size + offset
        
        
    return candidate

    

##def prime_wheel(max_wheel_size):
##    """ prime wheel has size equal to the largest
##    primorial (product of first n primes) less than max_wheel_size
##    and includes all moduli mod wheel_size that primes could take"""
##
##    # primorial (product of first k primes) has hard upper bound of 4^k
##    # primorials are precomputed in RSAprecompute.py
##    
##    # Find largest primorial less than max_wheel_size
##    prime_index = 0
##    wheel_size = RSAprecompute.primorials[prime_index]
##    next_wheel_size = RSAprecompute.primorials[prime_index+1]
##
##    while(next_wheel_size < max_wheel_size):
##        prime_index = prime_index+1
##        assert(prime_index < len(RSAprecompute.small_primes))
##        wheel_size = RSAprecompute.primorials[prime_index]
##        next_wheel_size = RSAprecompute.primorials[prime_index+1]
##
##    largest_prime = RSAprecompute.small_primes[prime_index]
##
##    return wheel(largest_prime, wheel_size)
##

def prime_wheel(prime_index):
    """ prime wheel has size equal to the largest
    primorial (product of first n primes) less than max_wheel_size
    and includes all moduli mod wheel_size that primes could take"""
    if(prime_index == 0):
        return [1]
    largest_prime = RSAprecompute.small_primes[prime_index]
    wheel_size = RSAprecompute.primorials[prime_index]

    return wheel(largest_prime, wheel_size)


def wheel(largest_prime, table_size):
    """ Returns moduli base table_size that primes could have """
    assert(largest_prime>=2)
    table = [False if (i%2==0) else True for i in range(table_size)]

    table[1] = True
    table[2] = False

    cur_prime = 3

    while(cur_prime <= largest_prime):
        # Knock out all multiples of largest confirmed prime.
        for i in range(cur_prime, table_size, cur_prime):
            table[i] = False

        # Advance to next prime
        cur_prime = cur_prime+2
        while(cur_prime == False):
            cur_prime = cur_prime+2
    # transfer boolean array
    # to array of possible prime offsets mod wheel_size
    wheel = []
    for i in range(1,table_size,2):
        if(table[i]):
            wheel.append(i)

    return wheel

def primorial(nth):
    """ calculates the nth primorial, or the product of the first n primes"""
    if(nth<len(RSAprecompute.small_primes)):
        result = 1
        for i in range(nth):
            result = result*RSAprecompute.small_primes[i]
        return result
    else:
        return -1 ####################################
            


def erat(largest_prime, table_size):
    """Sieve of Eratosthenes Algorithm.
    DOES NOT NECESSARILY GIVE ONLY PRIMES.
    values up to largest_prime^2 are prime, larger may not be."""
    assert(largest_prime>=2)
    table = [False if (i%2==0) else True for i in range(table_size)]

    table[1] = False
    table[2] = True

    cur_prime = 3

    while(cur_prime <= largest_prime):
        # Knock out all multiples of largest confirmed prime.
        for i in range(2*cur_prime, table_size, cur_prime):
            table[i] = False

        # Advance to next prime
        cur_prime = cur_prime+2
        while(cur_prime == False):
            cur_prime = cur_prime+2

    # transfer boolean array
    # to array of possible prime offsets mod wheel_size
    wheel = [2]
    for i in range(1,table_size,2):
        if(table[i]):
            wheel.append(i)

    return wheel

        
    
              
        

        

