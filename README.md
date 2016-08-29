# RSAchat
Familiarizing with RSA and building chat app

CONTENTS:
Real RSA.py - RSA functions for key generation, encryption, and decryption
RSAprimegen.py - functions associated with generating primes, most notably the factor wheel program
RSAhelp.py - helper functions used throughout: miller-rabin primality testing, modular exponentiation, modular multiplicative inverse
RSAprecompute.py - some precomputed primes, primorials, and factor wheels to try to get some runtime speedups


DEVELOPMENT PHASES:

PHASE 1:
ToyRSA - build working RSA with small constants
- generate keys
- encrypt number
- decrypt number

PHASE 2:
RealRSA - large numbers, randomly selected where appropriate
- Fast encryption and decryption using modular exponentation by squaring
- Key generation using random primes p,q:
  - find primes: use primorial-sized wheel factorization to limit search to possible prime moduli
  - probabilistic miller-rabin test to verify a randomly selected candidate is prime
  - fast modular multiplicative inverse using the extended Euclidean Algorithm

- Phase 2 next steps:
  - ASCII or UNICODE support
  - Randomized Padding scheme

PHASE 3:
MURSA - multi-user support
- User-facing features
  - basic (text-based) GUI
  - profiles
- multi-user features
  - group chat 
  - sidebar

PHASE 4:
Application
- Desktop/Mobile application
