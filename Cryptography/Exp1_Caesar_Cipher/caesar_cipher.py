"""
Experiment 1: Caesar Cipher Implementation
-------------------------------------------
Algorithm:
The Caesar cipher is a monoalphabetic substitution cipher where each letter 
in the plaintext is shifted by a fixed number of positions down the alphabet.

Mathematical Model:
- Encryption: C = (P + k) mod 26
- Decryption: P = (C - k) mod 26
where P is the plaintext character index (0-25), C is the ciphertext character index (0-25),
and k is the shift key.
"""

import sys

def caesar_encrypt(plaintext: str, shift: int) -> str:
    """Encrypts plaintext using Caesar Cipher with given shift key."""
    ciphertext = []
    for char in plaintext:
        if char.isupper():
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(shifted)
        elif char.islower():
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(shifted)
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypts ciphertext using Caesar Cipher with given shift key."""
    return caesar_encrypt(ciphertext, -shift)

def main():
    print("==================================================")
    print("        EXPERIMENT 1: CAESAR CIPHER               ")
    print("==================================================")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        plaintext = "HELLO WORLD CRYPTOGRAPHY LAB"
        shift = 3
        print(f"[+] Demo Mode Activated")
    else:
        plaintext = input("[+] Enter Plaintext: ")
        try:
            shift = int(input("[+] Enter Shift Key (integer): "))
        except ValueError:
            print("[-] Invalid key! Defaulting to shift key = 3.")
            shift = 3

    print(f"\n--- Input Parameters ---")
    print(f"Plaintext : {plaintext}")
    print(f"Shift Key : {shift}")

    # Encryption Process
    ciphertext = caesar_encrypt(plaintext, shift)
    print(f"\n--- Encryption Process ---")
    print(f"Formula   : C = (P + {shift}) mod 26")
    print(f"Encrypted Ciphertext: {ciphertext}")

    # Decryption Process
    decrypted_text = caesar_decrypt(ciphertext, shift)
    print(f"\n--- Decryption Process ---")
    print(f"Formula   : P = (C - {shift}) mod 26")
    print(f"Decrypted Plaintext : {decrypted_text}")

    print("\n[OK] SUCCESS: Caesar Cipher Encryption & Decryption Completed!")

if __name__ == "__main__":
    main()
