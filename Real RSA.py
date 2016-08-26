from RSAhelp import *

constP = 53
constQ = 59
constE = 65537


def generate_keys(bits):
    """generates public and private RSA keys with 'bits'-bit security"""
    p,q = generate_pq()     # select distinct (TODO:RANDOM) primes *p*,*q*
    n = p*q                 # modulus *n* for the keys
    phi_n = (p-1)*(q-1)
    e = generate_e(phi_n)   # public key exponent *e*
    d = generate_d(e, phi_n)# private key exponent *d*
    return ((n,e) , (n,d))  # return public and private modulus/exponent pairs

def generate_pq():
    """Selects two distinct prime numbers"""

    p = constP
    q = constQ

    while(not p):
        

    
    
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
  

def encrypt(mess, n, e):
    """ Encrypts message using public key.
TODO: implement square-and-multiply algorithm for fast mod exponentiation
"""
    enc = mess**e % n
    return enc

def decrypt(enc, n, d):
    """ Encrypts message using private key.
TODO: implement square-and-multiply algorithm for fast mod exponentiation
"""
    dec = enc**d % n
    return dec
