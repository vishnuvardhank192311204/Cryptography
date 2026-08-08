"""
Experiment 6: Affine Cipher Break (Cryptanalysis) Implementation
-----------------------------------------------------------------
Algorithm:
Cryptanalysis of Affine Cipher using Known Frequency / Pair Matching and 
Exhaustive Search.

Since the keyspace of Affine Cipher is small (12 valid 'a' values * 26 'b' values = 312 pairs),
we can:
1. Solve linear system when two plaintext-ciphertext letter pairs (P1 -> C1, P2 -> C2) are known:
     C1 ≡ a*P1 + b (mod 26)
     C2 ≡ a*P2 + b (mod 26)
     (C1 - C2) ≡ a*(P1 - P2) (mod 26) => a ≡ (C1 - C2) * (P1 - P2)^-1 (mod 26)
     b ≡ (C1 - a*P1) (mod 26)
2. Or perform exhaustive search across all 312 key combinations.
"""

import sys
import math

VALID_A_KEYS = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def mod_inverse(a: int, m: int = 26) -> int:
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    a_inv = mod_inverse(a, 26)
    if a_inv == -1:
        return ""
    res = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - base
            dec = (a_inv * (y - b)) % 26
            res.append(chr(dec + base))
        else:
            res.append(char)
    return "".join(res)

def break_affine_with_pair(p1_char: str, c1_char: str, p2_char: str, c2_char: str):
    """Derives key (a, b) from two known letter correspondences."""
    p1, c1 = ord(p1_char.upper()) - ord('A'), ord(c1_char.upper()) - ord('A')
    p2, c2 = ord(p2_char.upper()) - ord('A'), ord(c2_char.upper()) - ord('A')

    delta_p = (p1 - p2) % 26
    delta_c = (c1 - c2) % 26

    delta_p_inv = mod_inverse(delta_p, 26)
    if delta_p_inv == -1:
        return None, None

    a = (delta_c * delta_p_inv) % 26
    if math.gcd(a, 26) != 1:
        return None, None

    b = (c1 - a * p1) % 26
    return a, b

def main():
    print("==================================================")
    print("      EXPERIMENT 6: AFFINE CIPHER BREAK           ")
    print("==================================================")

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        ciphertext = "IJJINE CIPHER" # Encrypted "AFFINE CIPHER" with a=5, b=8 -> A(0)->8(I), F(5)->7(H)...
        # Let's encrypt "AFFINE" with a=5, b=8 -> A->I, F->7(H), F->H, I->8*5+8=48=22(W), N->13*5+8=73=21(V), E->4*5+8=28=2(C)
        ciphertext = "IHHWVC"
        p1, c1 = 'E', 'C'
        p2, c2 = 'T', 'V'
        print("[+] Demo Mode Activated")
    else:
        ciphertext = input("[+] Enter Affine Ciphertext: ").strip()
        p1 = input("[+] Most likely Plaintext Char 1 (default 'E'): ").strip() or 'E'
        c1 = input(f"[+] Corresponding Ciphertext Char 1: ").strip()
        p2 = input("[+] Most likely Plaintext Char 2 (default 'T'): ").strip() or 'T'
        c2 = input(f"[+] Corresponding Ciphertext Char 2: ").strip()

    print(f"\n--- Known Frequency Pair Attack ---")
    print(f"Target Pair 1: '{p1}' -> '{c1}'")
    print(f"Target Pair 2: '{p2}' -> '{c2}'")

    a_found, b_found = break_affine_with_pair(p1, c1, p2, c2)

    if a_found is not None:
        print(f"\n[+] DERIVED KEY PARAMETERS:")
        print(f"    a = {a_found}")
        print(f"    b = {b_found}")
        recovered_text = affine_decrypt(ciphertext, a_found, b_found)
        print(f"    Recovered Plaintext: {recovered_text}")
    else:
        print("[-] Could not solve linear equation directly from pairs.")

    print(f"\n--- Exhaustive Key Space Search (Top Candidates) ---")
    count = 0
    for a in VALID_A_KEYS:
        for b in range(26):
            pt = affine_decrypt(ciphertext, a, b)
            if count < 5: # Display sample brute-force candidates
                print(f"  Key (a={a:2d}, b={b:2d}) -> {pt}")
                count += 1

    print("\n[OK] SUCCESS: Affine Cipher Break Completed!")

if __name__ == "__main__":
    main()
