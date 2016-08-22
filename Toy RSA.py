
constP = 53
constQ = 59
constE = 65537


def generate_keys():
    p,q = generate_pq()     # select distinct (TODO:RANDOM) primes *p*,*q*
    n = p*q                 # modulus *n* for the keys
    phi_n = (p-1)*(q-1)
    e = generate_e(phi_n)   # public key exponent *e*
    d = generate_d(e, phi_n)# private key exponent *d*
    return ((n,e) , (n,d))  # return public and private modulus/exponent pairs

def generate_pq():
    """Selects two distinct prime numbers"""
    #TODO: use hash to pull randomly from table of large primes
    p = constP
    q = constQ
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
