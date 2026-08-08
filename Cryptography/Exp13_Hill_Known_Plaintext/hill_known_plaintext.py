"""
Experiment 13: Hill Cipher Known Plaintext Attack
--------------------------------------------------
Algorithm & Cryptanalysis Formulation:
In a Known Plaintext Attack on a 2x2 Hill Cipher, an attacker knows 2 pairs 
of plaintext blocks P and ciphertext blocks C.

Equations:
  C1 = P1 * K (mod 26)
  C2 = P2 * K (mod 26)

Combining into 2x2 matrices P and C:
  C = P * K (mod 26)
Multiplying by P^-1 on the left:
  K = P^-1 * C (mod 26)
"""

import sys
import numpy as np

def mod_inverse(a: int, m: int = 26) -> int:
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def matrix_mod_inv_2x2(M: np.ndarray) -> np.ndarray:
    det = int(np.round(np.linalg.det(M))) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv == -1:
        raise ValueError(f"Plaintext matrix det={det} is not invertible modulo 26!")
    adj = np.array([
        [M[1, 1], -M[0, 1]],
        [-M[1, 0], M[0, 0]]
    ]) % 26
    return (det_inv * adj) % 26

def recover_hill_key(p_text: str, c_text: str) -> np.ndarray:
    """Recovers 2x2 Key matrix K from known plaintext and ciphertext blocks."""
    p_vals = [ord(c.upper()) - ord('A') for c in p_text if c.isalpha()]
    c_vals = [ord(c.upper()) - ord('A') for c in c_text if c.isalpha()]

    if len(p_vals) < 4 or len(c_vals) < 4:
        raise ValueError("At least 4 characters (2 blocks) of Plaintext and Ciphertext required.")

    # Form 2x2 matrices P and C
    P = np.array([[p_vals[0], p_vals[1]], [p_vals[2], p_vals[3]]])
    C = np.array([[c_vals[0], c_vals[1]], [c_vals[2], c_vals[3]]])

    # K = P^-1 * C mod 26
    P_inv = matrix_mod_inv_2x2(P)
    K = np.dot(P_inv, C) % 26
    return P, C, P_inv, K

def main():
    print("==================================================")
    print("  EXPERIMENT 13: HILL KNOWN PLAINTEXT ATTACK      ")
    print("==================================================")

    # Demo default:
    # Key K = [[3, 3], [2, 5]]
    # Plaintext P = "HELP" -> H(7), E(4), L(11), P(15) -> P matrix = [[7, 4], [11, 15]]
    # Ciphertext C = "DPLE" -> D(3), P(15), L(11), E(4) -> C matrix = [[3, 15], [11, 4]]
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        known_plaintext = "HELP"
        known_ciphertext = "DPLE"
        print("[+] Demo Mode Activated")
    else:
        known_plaintext = input("[+] Enter Known Plaintext (>= 4 chars): ").strip()
        known_ciphertext = input("[+] Enter Corresponding Ciphertext (>= 4 chars): ").strip()

    try:
        P, C, P_inv, K_recovered = recover_hill_key(known_plaintext, known_ciphertext)
        
        print(f"\n--- Matrix Formulations ---")
        print(f"Plaintext Matrix P:")
        print(P)
        print(f"\nCiphertext Matrix C:")
        print(C)
        print(f"\nInverse Plaintext Matrix P^-1 mod 26:")
        print(P_inv)

        print(f"\n--- Recovered Key Matrix K (K = P^-1 * C mod 26) ---")
        print(K_recovered)
        print("\n[OK] SUCCESS: Hill Cipher Key Matrix Recovered!")

    except Exception as e:
        print(f"[-] Attack Failed: {e}")

if __name__ == "__main__":
    main()
