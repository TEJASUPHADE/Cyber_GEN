def permute(bits, pattern): return [bits[i - 1] for i in pattern]
def shift(l, n): return l[n:] + l[:n]
def xor(a, b): return [i ^ j for i, j in zip(a, b)]

S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

def sbox(bits, box):
    row = (bits[0]<<1) | bits[3]
    col = (bits[1]<<1) | bits[2]
    val = box[row][col]
    return [(val>>1)&1, val&1]

def fk(bits, key, step=''):
    EP = [4,1,2,3,2,3,4,1]
    P4 = [2,4,3,1]
    L, R = bits[:4], bits[4:]
    temp = xor(permute(R, EP), key)
    s_out = sbox(temp[:4], S0) + sbox(temp[4:], S1)
    p4 = permute(s_out, P4)
    result = xor(L, p4) + R
    print(f"{step}fk:\n  L = {L}, R = {R}\n  EP(R) ⊕ Key = {temp}\n  S-box output = {s_out}, P4 = {p4}\n  Result = {result}")
    return result

def keys(k):
    P10 = [3,5,2,7,4,10,1,9,8,6]
    P8 = [6,3,7,4,8,5,10,9]
    k = permute(k, P10)
    L, R = shift(k[:5], 1), shift(k[5:], 1)
    K1 = permute(L+R, P8)
    L, R = shift(L, 2), shift(R, 2)
    K2 = permute(L+R, P8)
    print(f"\nKey Generation:\n  P10 = {k}\n  K1  = {K1}\n  K2  = {K2}")
    return K1, K2

def encrypt(pt, k):
    IP, IPi = [2,6,3,1,4,8,5,7], [4,1,3,5,7,2,8,6]
    print(f"\nPlaintext = {pt}")
    K1, K2 = keys(k)
    pt = permute(pt, IP)
    print(f"\nAfter IP  = {pt}")
    pt = fk(pt, K1, 'Round 1 ')
    pt = pt[4:] + pt[:4]
    print(f"\nAfter swap = {pt}")
    pt = fk(pt, K2, 'Round 2 ')
    ct = permute(pt, IPi)
    print(f"\nAfter IP⁻¹ = {ct}")
    return ct

def str_to_bits(s):
    return [int(c) for c in s]

# --- USER INPUT ---
plain_str = input("Enter 8-bit plaintext (e.g. 10101010): ")
key_str = input("Enter 10-bit key (e.g. 1010000010): ")

# Input validation
if len(plain_str) != 8 or len(key_str) != 10 or not set(plain_str+key_str).issubset({'0', '1'}):
    print("Invalid input! Please enter correct bit lengths (8 for plaintext, 10 for key).")
else:
    pt = str_to_bits(plain_str)
    k = str_to_bits(key_str)
    cipher = encrypt(pt, k)
    print("\nFinal Cipher Text:", ''.join(map(str, cipher)))
