


def generate_keys():
    p,q = generate_pq()     # select distinct (TODO:RANDOM) primes *p*,*q*
    n = p*q                 # modulus *n* for the keys
    phi_n = (p-1)*(q-1)
    e = generate_e(phi_n)   # public key exponent *e*
    d = generate_d(e, phi_n)# private key exponent *d*
    return ((n,e) , (n,d)) # return public and private modulus/exponent pairs

def generate_pq():
    #TODO: use hash to pull randomly from table of large primes
    p = 23
    q = 27
    return p,q

