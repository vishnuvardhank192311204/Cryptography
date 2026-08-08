"""
Experiment 3: Playfair Cipher Implementation
---------------------------------------------
Algorithm:
The Playfair cipher is a manual symmetric encryption technique using digram substitution.
It constructs a 5x5 matrix of letters based on a keyword (combining 'I' and 'J').

Encryption Rules for Digram (char1, char2):
1. Same Row   : Replace each char with the char to its right (wrapping around).
2. Same Column: Replace each char with the char below it (wrapping around).
3. Rectangle  : Replace each char with the char in its own row and the other char's column.
"""

import sys

def prepare_playfair_matrix(key: str):
    """Constructs 5x5 matrix using keyword (combining I/J into I)."""
    key_clean = []
    seen = set()
    for c in key.upper():
        if c == 'J':
            c = 'I'
        if c.isalpha() and c not in seen:
            seen.add(c)
            key_clean.append(c)

    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ": # J excluded
        if c not in seen:
            seen.add(c)
            key_clean.append(c)

    matrix = [key_clean[i:i+5] for i in range(0, 25, 5)]
    pos_map = {}
    for r in range(5):
        for c in range(5):
            pos_map[matrix[r][c]] = (r, c)
    return matrix, pos_map

def prepare_plaintext(text: str) -> list:
    """Prepares text into digrams: replaces J with I, inserts filler 'X' for duplicates."""
    clean = [c.upper() if c.upper() != 'J' else 'I' for c in text if c.isalpha()]
    digrams = []
    i = 0
    while i < len(clean):
        c1 = clean[i]
        if i + 1 < len(clean):
            c2 = clean[i+1]
            if c1 == c2:
                digrams.append((c1, 'X'))
                i += 1
            else:
                digrams.append((c1, c2))
                i += 2
        else:
            digrams.append((c1, 'X'))
            i += 1
    return digrams

def playfair_encrypt(digrams: list, pos_map: dict, matrix: list) -> str:
    """Encrypts prepared digrams using Playfair matrix rules."""
    cipher_digrams = []
    for c1, c2 in digrams:
        r1, col1 = pos_map[c1]
        r2, col2 = pos_map[c2]

        if r1 == r2: # Same Row
            e1 = matrix[r1][(col1 + 1) % 5]
            e2 = matrix[r2][(col2 + 1) % 5]
        elif col1 == col2: # Same Column
            e1 = matrix[(r1 + 1) % 5][col1]
            e2 = matrix[(r2 + 1) % 5][col2]
        else: # Rectangle
            e1 = matrix[r1][col2]
            e2 = matrix[r2][col1]
        cipher_digrams.append(e1 + e2)
    return "".join(cipher_digrams)

def playfair_decrypt(ciphertext: str, pos_map: dict, matrix: list) -> str:
    """Decrypts Playfair ciphertext."""
    clean = [c.upper() for c in ciphertext if c.isalpha()]
    plain_digrams = []
    for i in range(0, len(clean), 2):
        c1, c2 = clean[i], clean[i+1]
        r1, col1 = pos_map[c1]
        r2, col2 = pos_map[c2]

        if r1 == r2: # Same Row
            p1 = matrix[r1][(col1 - 1) % 5]
            p2 = matrix[r2][(col2 - 1) % 5]
        elif col1 == col2: # Same Column
            p1 = matrix[(r1 - 1) % 5][col1]
            p2 = matrix[(r2 - 1) % 5][col2]
        else: # Rectangle
            p1 = matrix[r1][col2]
            p2 = matrix[r2][col1]
        plain_digrams.append(p1 + p2)
    return "".join(plain_digrams)

def main():
    print("==================================================")
    print("         EXPERIMENT 3: PLAYFAIR CIPHER            ")
    print("==================================================")

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        key = "MONARCHY"
        plaintext = "INSTRUMENTS"
        print("[+] Demo Mode Activated")
    else:
        key = input("[+] Enter Secret Keyword: ").strip()
        plaintext = input("[+] Enter Plaintext: ").strip()

    matrix, pos_map = prepare_playfair_matrix(key)

    print(f"\n--- Playfair 5x5 Matrix (Key: '{key.upper()}') ---")
    for row in matrix:
        print("  ".join(row))

    digrams = prepare_plaintext(plaintext)
    print(f"\n--- Digram Formatting ---")
    print(f"Formated Digrams: {digrams}")

    # Encrypt
    ciphertext = playfair_encrypt(digrams, pos_map, matrix)
    print(f"\n--- Encryption Process ---")
    print(f"Encrypted Ciphertext: {ciphertext}")

    # Decrypt
    decrypted = playfair_decrypt(ciphertext, pos_map, matrix)
    print(f"\n--- Decryption Process ---")
    print(f"Decrypted Ciphertext: {decrypted}")

    print("\n[OK] SUCCESS: Playfair Cipher Encryption & Decryption Completed!")

if __name__ == "__main__":
    main()
