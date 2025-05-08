# Diffie-Hellman Key Exchange

def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# --- User Inputs ---
p = int(input("Enter a prime number (p): "))           # e.g., 23
g = int(input("Enter a primitive root modulo p (g): ")) # e.g., 5

# Private keys (secret)
a = int(input("Enter Alice's private key: "))          # e.g., 6
b = int(input("Enter Bob's private key: "))            # e.g., 15

# Public keys
A = power(g, a, p)  # Alice sends this
B = power(g, b, p)  # Bob sends this

print(f"\nPublic Key of Alice (A = g^a mod p): {A}")
print(f"Public Key of Bob   (B = g^b mod p): {B}")

# Shared secret key (calculated by both)
s_alice = power(B, a, p)
s_bob = power(A, b, p)

print(f"\nShared Secret Key (computed by Alice): {s_alice}")
print(f"Shared Secret Key (computed by Bob)  : {s_bob}")
