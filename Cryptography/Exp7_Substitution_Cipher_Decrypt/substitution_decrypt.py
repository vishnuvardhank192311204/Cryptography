"""
Experiment 7: Substitution Cipher Decryption Tool
--------------------------------------------------
Algorithm:
This experiment provides a general monoalphabetic substitution decryption 
engine. Given a ciphertext and a 26-letter decryption key map (or substitution key), 
it performs character-by-character inverse mapping to recover the original plaintext.
"""

import sys
import string

STANDARD_ALPHABET = string.ascii_uppercase

def decrypt_substitution(ciphertext: str, key_map: dict) -> str:
    """Decrypts ciphertext using provided dictionary map."""
    decrypted = []
    for char in ciphertext:
        if char.isupper():
            decrypted.append(key_map.get(char, char))
        elif char.islower():
            decrypted.append(key_map.get(char.upper(), char).lower())
        else:
            decrypted.append(char)
    return "".join(decrypted)

def build_inverse_key_map(cipher_alphabet: str) -> dict:
    """Constructs mapping from Cipher Alphabet to Standard Alphabet."""
    return {cipher_alphabet[i]: STANDARD_ALPHABET[i] for i in range(26)}

def main():
    print("==================================================")
    print("  EXPERIMENT 7: SUBSTITUTION CIPHER DECRYPTION   ")
    print("==================================================")

    default_cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        ciphertext = "HKLLN VNKSZ"
        cipher_alphabet = default_cipher_alphabet
        print("[+] Demo Mode Activated")
    else:
        ciphertext = input("[+] Enter Ciphertext to Decrypt: ").strip()
        cipher_alphabet = input(f"[+] Enter 26-letter Substitution Key (default={default_cipher_alphabet}): ").strip().upper()
        if len(cipher_alphabet) != 26 or len(set(cipher_alphabet)) != 26:
            print("[-] Invalid key alphabet length/uniqueness. Defaulting to standard sample key.")
            cipher_alphabet = default_cipher_alphabet

    inv_map = build_inverse_key_map(cipher_alphabet)

    print(f"\n--- Inverse Key Map ---")
    print(f"Cipher Alphabet: {cipher_alphabet}")
    print(f"Plain Alphabet : {STANDARD_ALPHABET}")

    # Decryption
    plaintext = decrypt_substitution(ciphertext, inv_map)

    print(f"\n--- Decryption Execution ---")
    print(f"Input Ciphertext : {ciphertext}")
    print(f"Output Plaintext : {plaintext}")

    print("\n[OK] SUCCESS: Substitution Cipher Decryption Execution Completed!")

if __name__ == "__main__":
    main()
