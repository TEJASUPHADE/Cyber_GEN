from math import gcd

def modinv(a, m):
    # Extended Euclidean Algorithm
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def rsa():
    print("=== RSA Encryption & Decryption ===")

    # --- Inputs ---
    p = int(input("Enter a prime number p: "))   # e.g., 61
    q = int(input("Enter another prime q: "))    # e.g., 53

    if not (is_prime(p) and is_prime(q)):
        print("Both numbers must be prime!")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    e = int(input(f"Enter public key e (1 < e < {phi}, gcd(e, {phi})=1): "))
    if gcd(e, phi) != 1:
        print("Invalid e. It must be co-prime to φ(n).")
        return

    d = modinv(e, phi)

    print(f"\nPublic Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    # Message input
    msg = int(input("\nEnter message (as a number < n): "))
    if msg >= n:
        print("Message must be less than n.")
        return

    # Encryption
    cipher = pow(msg, e, n)
    print(f"Encrypted Cipher: {cipher}")

    # Decryption
    decrypted = pow(cipher, d, n)
    print(f"Decrypted Message: {decrypted}")

rsa()
