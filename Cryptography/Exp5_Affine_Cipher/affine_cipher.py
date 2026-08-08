"""
Experiment 5: Affine Cipher Implementation
-------------------------------------------
Algorithm:
The Affine cipher is a monoalphabetic substitution cipher where each character 
is encrypted using the mathematical function:
    E(x) = (a * x + b) mod 26
And decrypted using:
    D(x) = a_inv * (x - b) mod 26

Constraints:
- 'a' and 26 must be coprime: gcd(a, 26) == 1
- 'a_inv' is the modular multiplicative inverse of 'a' modulo 26 (a * a_inv ≡ 1 mod 26)
"""

import sys
import math

def mod_inverse(a: int, m: int = 26) -> int:
    """Computes modular multiplicative inverse of a mod m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    """Encrypts plaintext using Affine Cipher formula E(x) = (a*x + b) mod 26."""
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            enc = (a * x + b) % 26
            ciphertext.append(chr(enc + base))
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    """Decrypts ciphertext using Affine Cipher formula D(x) = a_inv * (x - b) mod 26."""
    a_inv = mod_inverse(a, 26)
    if a_inv == -1:
        raise ValueError(f"Key a={a} is not coprime with 26. Modular inverse does not exist.")

    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - base
            dec = (a_inv * (y - b)) % 26
            plaintext.append(chr(dec + base))
        else:
            plaintext.append(char)
    return "".join(plaintext)

def main():
    print("==================================================")
    print("           EXPERIMENT 5: AFFINE CIPHER            ")
    print("==================================================")

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        plaintext = "AFFINE CIPHER EXPERIMENT"
        a, b = 5, 8
        print("[+] Demo Mode Activated")
    else:
        plaintext = input("[+] Enter Plaintext: ").strip()
        try:
            a = int(input("[+] Enter key 'a' (coprime to 26, e.g. 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25): "))
            b = int(input("[+] Enter key 'b' (shift value 0-25): "))
        except ValueError:
            print("[-] Invalid input. Defaulting to a=5, b=8.")
            a, b = 5, 8

    if math.gcd(a, 26) != 1:
        print(f"[-] ERROR: gcd({a}, 26) = {math.gcd(a, 26)} != 1. Key 'a' must be coprime to 26.")
        return

    a_inv = mod_inverse(a, 26)
    print(f"\n--- Key Verification & Verification ---")
    print(f"Multiplicative Key (a) : {a}")
    print(f"Additive Key (b)       : {b}")
    print(f"gcd(a, 26)             : {math.gcd(a, 26)} [VALID]")
    print(f"Modular Inverse (a^-1) : {a_inv} (since {a} * {a_inv} ≡ 1 mod 26)")

    # Encrypt
    ciphertext = affine_encrypt(plaintext, a, b)
    print(f"\n--- Encryption Process ---")
    print(f"Formula   : E(x) = ({a} * x + {b}) mod 26")
    print(f"Ciphertext: {ciphertext}")

    # Decrypt
    decrypted = affine_decrypt(ciphertext, a, b)
    print(f"\n--- Decryption Process ---")
    print(f"Formula   : D(y) = {a_inv} * (y - {b}) mod 26")
    print(f"Decrypted : {decrypted}")

    print("\n[OK] SUCCESS: Affine Cipher Execution Completed!")

if __name__ == "__main__":
    main()
