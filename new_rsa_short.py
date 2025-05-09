from math import gcd

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def rsa():
    p = int(input("Prime p: "))
    q = int(input("Prime q: "))
    if not (is_prime(p) and is_prime(q)):
        print("Both must be prime.")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    e = int(input(f"Public key e (1 < e < {phi}): "))
    if gcd(e, phi) != 1:
        print("e must be co-prime to φ(n).")
        return

    d = modinv(e, phi)
    if d is None:
        print("Modular inverse not found.")
        return

    print(f"Public Key: ({e}, {n})")
    print(f"Private Key: ({d}, {n})")

    msg = int(input("Message (as int < n): "))
    if msg >= n:
        print("Message too large.")
        return

    cipher = pow(msg, e, n)
    plain = pow(cipher, d, n)

    print(f"Encrypted: {cipher}")
    print(f"Decrypted: {plain}")

rsa()




#for text 
from math import gcd

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def rsa():
    p = int(input("Prime p: "))
    q = int(input("Prime q: "))
    if not (is_prime(p) and is_prime(q)):
        print("Both must be prime.")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    e = int(input(f"Public key e (1 < e < {phi}): "))
    if gcd(e, phi) != 1:
        print("e must be co-prime to φ(n).")
        return

    d = modinv(e, phi)
    if d is None:
        print("Modular inverse not found.")
        return

    print(f"Public Key: ({e}, {n})")
    print(f"Private Key: ({d}, {n})")

    msg = int(input("Message (as int < n): "))
    if msg >= n:
        print("Message too large.")
        return

    cipher = pow(msg, e, n)
    plain = pow(cipher, d, n)

    print(f"Encrypted: {cipher}")
    print(f"Decrypted: {plain}")

rsa()
