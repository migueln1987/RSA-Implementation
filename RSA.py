# Miguel Najera

from random import getrandbits

def generateKeys():
    p = getrandbits(2048)
    q = getrandbits(2048)
    while not is_prime(p):
        p = getrandbits(2048)
    while not is_prime(q):
        q = getrandbits(2048)
    m = p * q
    n = (p - 1) * (q - 1)
    for i in range(2, (n)):
        if gcd(i,n) == 1:
            e = i
            break
    d = modInverse(e, n)
    return p, q, n, m, e, d


def encrypt(integer, e, m):
    encryptedInteger = pow(integer, e, m)
    return encryptedInteger

def decrypt(integer, d, m):
    decryptedInteger = pow(integer, d, m)
    return decryptedInteger

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def modInverse(a, n):
    t = 0
    newT = 1
    r = n
    newR = a
    while newR != 0:
        quotient = r // newR
        t, newT = newT, t - quotient * newT
        r, newR = newR, r - quotient * newR
    if r > 1:
        return 0
    if t < 0:
        t += n
    return t

""" Miller-Rabin Primality Test 
    [http://rosettacode.org](http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python:_Proved_correct_up_to_large_N) """
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True

def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0,1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2,3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    return not any(_try_composite(a, d, n, s) for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2,3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

def main():
    p, q, n, m, e, d = generateKeys()
    print("p = " + str(p) + "\n")
    print("q = " + str(q) + "\n")
    print("n = " + str(n) + "\n")
    print("m = " + str(m) + "\n")
    print("e = " + str(e) + "\n")
    print("d = " + str(d) + "\n")
    integer = getrandbits(2048)
    while not integer < m:
        integer = getrandbits(2048)
    print("Plaintext: " + str(integer) + "\n")
    encryptedInteger = encrypt(integer, e, m)
    print("Encrypted: " + str(encryptedInteger) + "\n")
    decryptedInteger = decrypt(encryptedInteger, d, m)
    print("Decrypted: " + str(decryptedInteger) + "\n")

if __name__ == "__main__":
    main()
      
