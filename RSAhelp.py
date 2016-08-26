# RSAhelp.py
# This is a file for helper functions involved in RSA
# including:
# - fast modular exponentiation
# - fast modular multiplicative inverse
# - miller-rabin primality testing
# - wrapper funct for generating cryptographic numbers of arbitrary size
# - generating random primes of arbitrary size

from os import urandom
import math

def mod_exp(base, expo, mod):
    """Fast exponentiation in O(log(expo)) time by
       repeatedly squaring base and taking the result modulo 'mod' """

    result = 1 # result holds the "odd-man out" factors
    while(expo>0):
        if(expo % 2 == 1):
            result = (result * base) % mod
        expo = expo >> 1 # integer division by 2
        base = (base * base) % mod # base holds base^(2i)
    return result

def mod_mult_inv(a, mod):
    """find the mult inverse of e mod phi_n using euclidean alg"""
    # used pseduocode on extended euclidean algorithm from wikipedia
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Computing_multiplicative_inverses_in_modular_structures
    t = 0
    new_t=1
    r = mod
    new_r = a

    while(new_r != 0):
        quotient = r/new_r
        (t, new_t) = (new_t, t - quotient*new_t)
        (r, new_r) = (new_r, r - quotient*new_r)
    if (r>1): print("e and phi_n are not coprime")
    if (t<0): t = t+mod
    return t

BYTE_BITS = 8


def crypto_rand(*args):
    num_args = len(args)
    low = 0
    if num_args == 1:
        high = args[0]
    else:
        low = args[0]
        high = args[1]
        assert(low<high)

    result = -1
    while(result<low or result>=high):
        bits = math.ceil(math.log(high,2))
        num_bytes = math.ceil(bits/BYTE_BITS)
        result = int.from_bytes(urandom(num_bytes),'big')>>(bits%BYTE_BITS)    
    return result


##########################################################
#### MILLER-RABIN PRIMALITY TEST #########################
##########################################################

BYTE_SIZE = 256 # number of values that can be held by a byte


def miller_rabin(n, k=15):
    """miller_rabin probabalistically tests input n for primality.
    Parameter k gives the confidence.
    False positives are reported with likelihood 4^(-k)."""

    if(n==3 or n==2):
        return True
    elif(n<2 or n%2==0):
        return False
    
    # represent n-1 as 2^r * d for maximal r
    nmin1 = n-1
    d = nmin1
    r = 0
    while(d % 2 == 0):
        r = r+1
        d = int(d/2)

    # Decide necessary number of witnesses, k
    # False positives occur with probability k^(-4)
    # k = 15 gives better than 1 in 1 billion odds

    # run k tests:
    for  i in range(k):
        a=0
        # select witness a randomly in range [2,n-2]
        a = 0
        while(a<2):
            a = crypto_rand(2,n-1)

        if(not witness_test(a, n, d, r)):
            return False
    
    return True


def witness_test(a, n, d, r):
    """performs single-witness miller-rabin test
       false - composite. true - probably prime."""
    nmin1 = n-1
    x = mod_exp(a, d, n)
    if(x==1 or x==nmin1):
        return True
    for j in range(r-1):
        x = mod_exp(x, 2, n)
        if(x == 1):
            return False
        elif(x == nmin1):
            return True
    return False



#######################################################
### Prime generation ##################################
#######################################################

def retry_until_prime(low, high):
    """NAIVE: finds primes by picking numbers at random and checking"""
    p = 1
    prime = False
    while(not prime):
        p = crypto_rand(low,high)
        print(p)
        prime = miller_rabin(p)
    return p
              
        

        

