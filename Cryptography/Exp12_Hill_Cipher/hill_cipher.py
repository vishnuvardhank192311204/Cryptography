"""
Experiment 12: Hill Cipher Implementation
-------------------------------------------
Algorithm:
The Hill cipher is a multigraphic substitution cipher based on linear algebra.

Mathematical Formulation (2x2 Matrix):
- Encryption : C = (P * K) mod 26
- Decryption : P = (C * K^-1) mod 26

Key Matrix K:
  [ k11  k12 ]
  [ k21  k22 ]

Determinant det(K) = (k11*k22 - k12*k21) mod 26
Inverse Matrix K^-1 = det_inv * adj(K) mod 26
where adj(K) = [  k22  -k12 ]
               [ -k21   k11 ]
"""

import sys
import numpy as np

def mod_inverse(a: int, m: int = 26) -> int:
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def matrix_mod_inv_2x2(K: np.ndarray) -> np.ndarray:
    """Calculates 2x2 matrix inverse modulo 26."""
    det = int(np.round(np.linalg.det(K))) % 26
    det_inv = mod_inverse(det, 26)
    
    if det_inv == -1:
        raise ValueError(f"Determinant det(K)={det} is not coprime with 26. Key matrix is non-invertible!")

    # Adjugate matrix for 2x2: [[d, -b], [-c, a]]
    adj = np.array([
        [K[1, 1], -K[0, 1]],
        [-K[1, 0], K[0, 0]]
    ]) % 26

    K_inv = (det_inv * adj) % 26
    return K_inv

def hill_encrypt(plaintext: str, K: np.ndarray) -> str:
    """Encrypts plaintext using 2x2 Hill Cipher."""
    clean_p = [ord(c.upper()) - ord('A') for c in plaintext if c.isalpha()]
    if len(clean_p) % 2 != 0:
        clean_p.append(ord('X') - ord('A')) # Padding

    ciphertext = []
    for i in range(0, len(clean_p), 2):
        block = np.array(clean_p[i:i+2])
        enc_block = np.dot(block, K) % 26
        ciphertext.extend(enc_block)

    return "".join(chr(int(c) + ord('A')) for c in ciphertext)

def hill_decrypt(ciphertext: str, K: np.ndarray) -> str:
    """Decrypts ciphertext using 2x2 Hill Cipher."""
    K_inv = matrix_mod_inv_2x2(K)
    clean_c = [ord(c.upper()) - ord('A') for c in ciphertext if c.isalpha()]

    plaintext = []
    for i in range(0, len(clean_c), 2):
        block = np.array(clean_c[i:i+2])
        dec_block = np.dot(block, K_inv) % 26
        plaintext.extend(dec_block)

    return "".join(chr(int(p) + ord('A')) for p in plaintext)

def main():
    print("==================================================")
    print("           EXPERIMENT 12: HILL CIPHER             ")
    print("==================================================")

    # Key Matrix K = [[3, 3], [2, 5]] (det = 15 - 6 = 9, gcd(9, 26)=1, det_inv = 3)
    default_K = np.array([[3, 3], [2, 5]])

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        plaintext = "HELP"
        K = default_K
        print("[+] Demo Mode Activated")
    else:
        plaintext = input("[+] Enter Plaintext: ").strip()
        print("[+] Enter 2x2 Key Matrix elements (row by row):")
        try:
            k11 = int(input("    k11: "))
            k12 = int(input("    k12: "))
            k21 = int(input("    k21: "))
            k22 = int(input("    k22: "))
            K = np.array([[k11, k12], [k21, k22]])
        except ValueError:
            print("[-] Invalid input. Defaulting to Key Matrix [[3, 3], [2, 5]].")
            K = default_K

    det = int(np.round(np.linalg.det(K))) % 26
    det_inv = mod_inverse(det, 26)

    print(f"\n--- Key Matrix K ---")
    print(K)
    print(f"det(K) mod 26        : {det}")
    print(f"det(K)^-1 mod 26     : {det_inv}")

    if det_inv == -1:
        print("[-] ERROR: Key matrix is not invertible modulo 26! gcd(det, 26) != 1.")
        return

    K_inv = matrix_mod_inv_2x2(K)
    print(f"\n--- Inverse Key Matrix K^-1 mod 26 ---")
    print(K_inv)

    # Encryption
    ciphertext = hill_encrypt(plaintext, K)
    print(f"\n--- Encryption Process ---")
    print(f"Plaintext : {plaintext}")
    print(f"Ciphertext: {ciphertext}")

    # Decryption
    decrypted = hill_decrypt(ciphertext, K)
    print(f"\n--- Decryption Process ---")
    print(f"Decrypted : {decrypted}")

    print("\n[OK] SUCCESS: Hill Cipher Encryption & Decryption Completed!")

if __name__ == "__main__":
    main()
