# RSAchat
Familiarizing with RSA and building chat app

DEVELOPMENT PHASES:

PHASE 1:
ToyRSA - build "working" RSA with small constants
- generate keys
- encrypt number
- decrypt number
- basic padding for ascii

PHASE 2:
RealRSA - large numbers, randomly selected where appropriate
- sieve (eratosthenes, atkin) to create table of large primes
- instead of sieve, probabalistic randomness tests (Miller-Rabin/Fermat)
- random selection of p,q
- sufficiently large e,d
- encryption and decryption of large messages

PHASE 3:
MURSA - multi-user support
- application
- additional features
  - group chat (if this isn't unsolved)
  - sidebar
- multi-device use for single user with multi-factor identification.
