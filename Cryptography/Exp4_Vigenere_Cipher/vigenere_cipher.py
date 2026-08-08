"""
Experiment 4: Vigenère Cipher Implementation
---------------------------------------------
Algorithm:
The Vigenère cipher is a method of encrypting alphabetic text by using a series 
of interwoven Caesar ciphers, based on the letters of a keyword.

Mathematical Formulation:
- Encryption: C_i = (P_i + K_i) mod 26
- Decryption: P_i = (C_i - K_i + 26) mod 26
where P_i is plaintext char index, K_i is keyword char index, C_i is ciphertext char index.
"""

import sys

def vigenere_encrypt(plaintext: str, key: str) -> (str, str):
    """Encrypts plaintext using Vigenère Cipher with key repeating."""
    clean_p = [c.upper() for c in plaintext if c.isalpha()]
    clean_k = [c.upper() for c in key if c.isalpha()]
    
    if not clean_k:
        raise ValueError("Keyword must contain alphabetic characters.")

    repeated_key = [clean_k[i % len(clean_k)] for i in range(len(clean_p))]
    
    ciphertext = []
    for p, k in zip(clean_p, repeated_key):
        c_idx = (ord(p) - ord('A') + (ord(k) - ord('A'))) % 26
        ciphertext.append(chr(c_idx + ord('A')))
        
    return "".join(ciphertext), "".join(repeated_key)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """Decrypts Vigenère ciphertext using key."""
    clean_c = [c.upper() for c in ciphertext if c.isalpha()]
    clean_k = [c.upper() for c in key if c.isalpha()]
    
    repeated_key = [clean_k[i % len(clean_k)] for i in range(len(clean_c))]
    
    plaintext = []
    for c, k in zip(clean_c, repeated_key):
        p_idx = (ord(c) - ord('A') - (ord(k) - ord('A')) + 26) % 26
        plaintext.append(chr(p_idx + ord('A')))
        
    return "".join(plaintext)

def main():
    print("==================================================")
    print("         EXPERIMENT 4: VIGENÈRE CIPHER            ")
    print("==================================================")

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        plaintext = "GEEKSFORGEEKS"
        key = "AYUSH"
        print("[+] Demo Mode Activated")
    else:
        plaintext = input("[+] Enter Plaintext: ").strip()
        key = input("[+] Enter Keyword: ").strip()

    ciphertext, repeated_key = vigenere_encrypt(plaintext, key)

    print(f"\n--- Alignment & Key Expansion ---")
    print(f"Plaintext   : {' '.join([c.upper() for c in plaintext if c.isalpha()])}")
    print(f"Repeated Key: {' '.join(repeated_key)}")

    print(f"\n--- Encryption Process ---")
    print(f"Formula   : C_i = (P_i + K_i) mod 26")
    print(f"Ciphertext: {ciphertext}")

    decrypted = vigenere_decrypt(ciphertext, key)
    print(f"\n--- Decryption Process ---")
    print(f"Formula   : P_i = (C_i - K_i) mod 26")
    print(f"Decrypted : {decrypted}")

    print("\n[OK] SUCCESS: Vigenère Cipher Encryption & Decryption Completed!")

if __name__ == "__main__":
    main()
