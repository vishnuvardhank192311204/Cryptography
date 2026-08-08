"""
Experiment 2: Monoalphabetic Substitution Cipher Implementation
----------------------------------------------------------------
Algorithm:
The Monoalphabetic cipher replaces each character of the plain text with another 
character based on a fixed 26-letter substitution key alphabet.

Key properties:
- Plain Alphabet : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
- Cipher Alphabet: A permuted ordering of the 26 English letters.
"""

import sys
import string

STANDARD_ALPHABET = string.ascii_uppercase

def monoalphabetic_encrypt(plaintext: str, cipher_key: str) -> str:
    """Encrypts plaintext using monoalphabetic substitution mapping."""
    key_map = {STANDARD_ALPHABET[i]: cipher_key[i] for i in range(26)}
    ciphertext = []
    for char in plaintext:
        if char.isupper():
            ciphertext.append(key_map.get(char, char))
        elif char.islower():
            ciphertext.append(key_map.get(char.upper(), char).lower())
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def monoalphabetic_decrypt(ciphertext: str, cipher_key: str) -> str:
    """Decrypts ciphertext using inverse monoalphabetic substitution mapping."""
    inv_map = {cipher_key[i]: STANDARD_ALPHABET[i] for i in range(26)}
    plaintext = []
    for char in ciphertext:
        if char.isupper():
            plaintext.append(inv_map.get(char, char))
        elif char.islower():
            plaintext.append(inv_map.get(char.upper(), char).lower())
        else:
            plaintext.append(char)
    return "".join(plaintext)

def main():
    print("==================================================")
    print("    EXPERIMENT 2: MONOALPHABETIC CIPHER           ")
    print("==================================================")

    # Standard default substitution key mapping
    default_key = "QWERTYUIOPASDFGHJKLZXCVBNM"

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        plaintext = "SECURITY AND CRYPTOGRAPHY"
        cipher_key = default_key
        print("[+] Demo Mode Activated")
    else:
        plaintext = input("[+] Enter Plaintext: ")
        cipher_key_in = input(f"[+] Enter 26-letter Cipher Key (default={default_key}): ").strip().upper()
        if len(cipher_key_in) == 26 and len(set(cipher_key_in)) == 26 and cipher_key_in.isalpha():
            cipher_key = cipher_key_in
        else:
            print("[-] Invalid key entered. Using default permutation key.")
            cipher_key = default_key

    print(f"\n--- Substitution Key Mapping ---")
    print(f"Plain Alphabet : {STANDARD_ALPHABET}")
    print(f"Cipher Alphabet: {cipher_key}")

    print(f"\n--- Input Parameters ---")
    print(f"Plaintext : {plaintext}")

    # Encryption
    ciphertext = monoalphabetic_encrypt(plaintext, cipher_key)
    print(f"\n--- Encryption Process ---")
    print(f"Encrypted Ciphertext: {ciphertext}")

    # Decryption
    decrypted = monoalphabetic_decrypt(ciphertext, cipher_key)
    print(f"\n--- Decryption Process ---")
    print(f"Decrypted Plaintext : {decrypted}")

    print("\n[OK] SUCCESS: Monoalphabetic Cipher Execution Completed!")

if __name__ == "__main__":
    main()
