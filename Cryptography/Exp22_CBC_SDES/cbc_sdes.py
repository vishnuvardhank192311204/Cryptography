# S-DES Implementation and CBC Mode
# P10, P8, IP, EP, P4, IP_inv tables
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]

S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

def permute(bits, table):
    return [bits[i-1] for i in table]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def key_generation(key):
    k = permute(key, P10)
    L, R = k[:5], k[5:]
    L, R = left_shift(L, 1), left_shift(R, 1)
    k1 = permute(L + R, P8)
    L, R = left_shift(L, 2), left_shift(R, 2)
    k2 = permute(L + R, P8)
    return k1, k2

def sbox(bits, sbox_matrix):
    row = (bits[0] << 1) | bits[3]
    col = (bits[1] << 1) | bits[2]
    val = sbox_matrix[row][col]
    return [(val >> 1) & 1, val & 1]

def f_k(bits, key):
    L, R = bits[:4], bits[4:]
    R_exp = permute(R, EP)
    xor_res = [r ^ k for r, k in zip(R_exp, key)]
    s0_res = sbox(xor_res[:4], S0)
    s1_res = sbox(xor_res[4:], S1)
    p4_res = permute(s0_res + s1_res, P4)
    new_L = [l ^ p for l, p in zip(L, p4_res)]
    return new_L + R

def sdes_encrypt(pt, k1, k2):
    bits = permute(pt, IP)
    bits = f_k(bits, k1)
    bits = bits[4:] + bits[:4] # SW
    bits = f_k(bits, k2)
    return permute(bits, IP_inv)

def sdes_decrypt(ct, k1, k2):
    bits = permute(ct, IP)
    bits = f_k(bits, k2)
    bits = bits[4:] + bits[:4] # SW
    bits = f_k(bits, k1)
    return permute(bits, IP_inv)

def to_bits(binary_str):
    return [int(c) for c in binary_str]

def to_str(bits):
    return "".join(str(b) for b in bits)

def xor_lists(l1, l2):
    return [a ^ b for a, b in zip(l1, l2)]

def main():
    print("--- CBC S-DES Demonstration ---")
    iv_str = "10101010"
    pt_str = "0000000100100011"
    key_str = "0111111101"
    expected_ct_str = "1111010000001011"
    
    key = to_bits(key_str)
    iv = to_bits(iv_str)
    
    k1, k2 = key_generation(key)
    
    # Split PT into two 8-bit blocks
    pt_blocks = [to_bits(pt_str[:8]), to_bits(pt_str[8:])]
    
    print(f"IV: {iv_str}")
    print(f"Plaintext: {pt_str[:8]} {pt_str[8:]}")
    print(f"Key: {key_str}\n")
    
    # CBC Encrypt
    ct_blocks = []
    prev_ct = iv
    for pt in pt_blocks:
        xored = xor_lists(pt, prev_ct)
        ct = sdes_encrypt(xored, k1, k2)
        ct_blocks.append(ct)
        prev_ct = ct
        
    final_ct_str = to_str(ct_blocks[0]) + to_str(ct_blocks[1])
    print(f"Encrypted Ciphertext: {final_ct_str[:8]} {final_ct_str[8:]}")
    print(f"Expected Ciphertext : {expected_ct_str[:8]} {expected_ct_str[8:]}")
    
    if final_ct_str == expected_ct_str:
        print("Encryption: PASS")
    else:
        print("Encryption: FAIL")
        
    # CBC Decrypt
    dec_blocks = []
    prev_ct = iv
    for ct in ct_blocks:
        dec = sdes_decrypt(ct, k1, k2)
        pt = xor_lists(dec, prev_ct)
        dec_blocks.append(pt)
        prev_ct = ct
        
    final_pt_str = to_str(dec_blocks[0]) + to_str(dec_blocks[1])
    print(f"\nDecrypted Plaintext : {final_pt_str[:8]} {final_pt_str[8:]}")
    print(f"Original Plaintext  : {pt_str[:8]} {pt_str[8:]}")
    if final_pt_str == pt_str:
        print("Decryption: PASS")
    else:
        print("Decryption: FAIL")

if __name__ == "__main__":
    main()
