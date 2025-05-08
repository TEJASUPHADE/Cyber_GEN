# S-AES helper functions and constants
SBOX = [0x9, 0x4, 0xA, 0xB,
        0xD, 0x1, 0x8, 0x5,
        0x6, 0x2, 0x0, 0x3,
        0xC, 0xE, 0xF, 0x7]

SBOX_INV = [0xA, 0x5, 0x9, 0xB,
            0x1, 0x7, 0x8, 0xF,
            0x6, 0x0, 0x2, 0x3,
            0xC, 0x4, 0xD, 0xE]

RCON1 = 0x80
RCON2 = 0x30

def sub_nib(b): return (SBOX[b >> 4] << 4) + SBOX[b & 0x0F]
def sub_nib_inv(b): return (SBOX_INV[b >> 4] << 4) + SBOX_INV[b & 0x0F]

def rot_nib(b): return ((b << 4) | (b >> 4)) & 0xFF

def key_expand(key):
    w = [0]*6
    w[0] = (key >> 8) & 0xFF
    w[1] = key & 0xFF
    w[2] = w[0] ^ RCON1 ^ sub_nib(rot_nib(w[1]))
    w[3] = w[2] ^ w[1]
    w[4] = w[2] ^ RCON2 ^ sub_nib(rot_nib(w[3]))
    w[5] = w[4] ^ w[3]
    return [((w[i] << 8) | w[i+1]) for i in range(0, 6, 2)]

def mult(p1, p2):
    p = 0
    for i in range(4):
        if p2 & 0x1:
            p ^= p1
        hi_bit_set = p1 & 0x8
        p1 = (p1 << 1) & 0xF
        if hi_bit_set:
            p1 ^= 0x3
        p2 >>= 1
    return p

def mix_columns(s):
    return ((mult(s >> 12, 1) << 12) ^ (mult((s >> 8) & 0xF, 4) << 8) ^
            (mult((s >> 4) & 0xF, 4) << 4) ^ (mult(s & 0xF, 1)))

def mix_columns_inv(s):
    return ((mult(s >> 12, 9) << 12) ^ (mult((s >> 8) & 0xF, 2) << 8) ^
            (mult((s >> 4) & 0xF, 2) << 4) ^ (mult(s & 0xF, 9)))

def encrypt(ptext, key):
    keys = key_expand(key)
    state = ptext ^ keys[0]
    state = sub_nib(state >> 8) << 8 | sub_nib(state & 0xFF)
    state = (state & 0xF0F0) >> 4 | (state & 0x0F0F) << 4  # ShiftRows
    state = mix_columns(state)
    state ^= keys[1]
    state = sub_nib(state >> 8) << 8 | sub_nib(state & 0xFF)
    state = (state & 0xF0F0) >> 4 | (state & 0x0F0F) << 4  # ShiftRows
    state ^= keys[2]
    return state

# --- USER INPUT VERSION ---
def get_input():
    pt_hex = input("Enter 16-bit plaintext in hex (e.g., 1234): ")
    key_hex = input("Enter 16-bit key in hex (e.g., abcd): ")
    try:
        pt = int(pt_hex, 16)
        key = int(key_hex, 16)
        if 0 <= pt <= 0xFFFF and 0 <= key <= 0xFFFF:
            ct = encrypt(pt, key)
            print(f"\nEncrypted Ciphertext = {hex(ct)[2:].zfill(4)}")
        else:
            print("Values must be 16-bit (0000 to FFFF).")
    except ValueError:
        print("Invalid input. Please enter valid hexadecimal values.")

get_input()
