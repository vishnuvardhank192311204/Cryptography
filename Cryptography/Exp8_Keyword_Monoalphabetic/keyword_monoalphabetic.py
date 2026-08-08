"""
Experiment 8: Keyword Monoalphabetic Cipher Implementation
------------------------------------------------------------
Algorithm:
The Keyword Monoalphabetic Cipher derives a substitution alphabet from a secret 
keyword. 
1. Write down unique letters of the keyword.
2. Fill the remaining slots of the 26-letter cipher alphabet with unused English 
   letters in standard alphabetical order.
"""

import sys
import string

STANDARD_ALPHABET = string.ascii_uppercase

def generate_keyword_alphabet(keyword: str) -> str:
    """Generates 26-letter substitution alphabet using keyword prefix."""
    cipher_alphabet = []
    seen = set()
    
    # 1. Add unique characters from keyword
    for char in keyword.upper():
        if char.isalpha() and char not in seen:
            seen.add(char)
            cipher_alphabet.append(char)
            
    # 2. Append remaining un-used alphabet characters
    for char in STANDARD_ALPHABET:
        if char not in seen:
            seen.add(char)
            cipher_alphabet.append(char)
            
    return "".join(cipher_alphabet)

def keyword_encrypt(plaintext: str, cipher_alphabet: str) -> str:
    """Encrypts plaintext using keyword substitution alphabet."""
    key_map = {STANDARD_ALPHABET[i]: cipher_alphabet[i] for i in range(26)}
    res = []
    for c in plaintext:
        if c.isupper():
            res.append(key_map.get(c, c))
        elif c.islower():
            res.append(key_map.get(c.upper(), c).lower())
        else:
            res.append(c)
    return "".join(res)

def keyword_decrypt(ciphertext: str, cipher_alphabet: str) -> str:
    """Decrypts ciphertext using inverse keyword substitution alphabet."""
    inv_map = {cipher_alphabet[i]: STANDARD_ALPHABET[i] for i in range(26)}
    res = []
    for c in ciphertext:
        if c.isupper():
            res.append(inv_map.get(c, c))
        elif c.islower():
            res.append(inv_map.get(c.upper(), c).lower())
        else:
            res.append(c)
    return "".join(res)

def main():
    print("==================================================")
    print("    EXPERIMENT 8: KEYWORD MONOALPHABETIC CIPHER   ")
    print("==================================================")

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        keyword = "KRYPTOS"
        plaintext = "SECRET ASSIGNMENT SUBMISSION"
        print("[+] Demo Mode Activated")
    else:
        keyword = input("[+] Enter Keyword: ").strip()
        plaintext = input("[+] Enter Plaintext: ").strip()

    cipher_alphabet = generate_keyword_alphabet(keyword)

    print(f"\n--- Cipher Alphabet Construction ---")
    print(f"Keyword          : {keyword}")
    print(f"Plain Alphabet   : {STANDARD_ALPHABET}")
    print(f"Cipher Alphabet  : {cipher_alphabet}")

    # Encrypt
    ciphertext = keyword_encrypt(plaintext, cipher_alphabet)
    print(f"\n--- Encryption Process ---")
    print(f"Ciphertext: {ciphertext}")

    # Decrypt
    decrypted = keyword_decrypt(ciphertext, cipher_alphabet)
    print(f"\n--- Decryption Process ---")
    print(f"Decrypted : {decrypted}")

    print("\n[OK] SUCCESS: Keyword Monoalphabetic Cipher Completed!")

if __name__ == "__main__":
    main()
