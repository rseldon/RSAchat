from RSAhelp import *
from RSAprimegen import *

constP = 1021
constQ = 1009
constE = 65537
WHEELDEGREE = 0


def generate_keys(bits=128):
    """generates public and private RSA keys with 'bits'-bit security"""
    p,q = generate_pq(bits) # select distinct (TODO:RANDOM) primes *p*,*q*
    n = p*q                 # modulus *n* for the keys

    while(n<2**(bits-1)):
        p,q = generate_pq(bits)
        print("trying again")
        
    phi_n = (p-1)*(q-1)
    e = generate_e(phi_n)   # public key exponent *e*
    d = generate_d(e, phi_n)# private key exponent *d*
    return ((n,e) , (n,d))  # return public and private modulus/exponent pairs

def generate_pq(bits=128):
    """Selects two distinct prime numbers"""

    low = math.floor(2 ** ((bits-1)/2))
    high = math.floor(2 ** (bits/2))
    
    p = wheel_find_prime(low, high, WHEELDEGREE)
    q = wheel_find_prime(low, high, WHEELDEGREE)

    return p,q

def generate_e(phi_n):
    """Selects a value for *e*, the public key explonent.
Must be coprime with phi_n.
"""
    e = constE
    if(phi_n % e == 0): print("e not coprime to phi_n")
    return constE

def generate_d(e, phi_n):
    """set *d* as multiplicative inverse of e mod phi_n"""
    d = mod_mult_inv(e, phi_n)
    return d
  

def encrypt(mess, pub):
    """ Encrypts message using private key.
    Uses square-and-multiply algorithm for fast mod exponentiation
    """
    e = pub[1]
    n = pub[0]
    enc = mod_exp(mess,e,n)
    return enc

def decrypt(enc, priv):
    """ Decrypts message using private key.
    Uses square-and-multiply algorithm for fast mod exponentiation
    """
    d = priv[1]
    n = priv[0]
    dec = mod_exp(enc,d,n)
    return dec
