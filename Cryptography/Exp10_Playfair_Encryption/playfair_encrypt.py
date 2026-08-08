"""
Experiment 10: Playfair Cipher Encryption Detailed Visualizer
--------------------------------------------------------------
Algorithm:
Provides a step-by-step visual trace of the Playfair Encryption process:
1. Matrix Construction (5x5, I/J merged).
2. Digram Preparation (pair splitting & filler 'X' insertion).
3. Detailed Step-by-Step Rule Evaluation for each digram.
"""

import sys

def build_matrix(key: str):
    clean = []
    seen = set()
    for c in key.upper():
        if c == 'J': c = 'I'
        if c.isalpha() and c not in seen:
            seen.add(c)
            clean.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in seen:
            seen.add(c)
            clean.append(c)
    matrix = [clean[i:i+5] for i in range(0, 25, 5)]
    pos_map = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    return matrix, pos_map

def format_digrams(text: str) -> list:
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

def detailed_playfair_encrypt(text: str, key: str):
    matrix, pos_map = build_matrix(key)
    digrams = format_digrams(text)
    
    print(f"\n--- Step 1: 5x5 Key Matrix ('{key.upper()}') ---")
    for row in matrix:
        print("  ".join(row))

    print(f"\n--- Step 2: Digram Formatting ---")
    print(f"Digrams: {digrams}")

    print(f"\n--- Step 3: Digram Transformation Trace ---")
    cipher_digrams = []
    for idx, (c1, c2) in enumerate(digrams, 1):
        r1, col1 = pos_map[c1]
        r2, col2 = pos_map[c2]

        if r1 == r2:
            e1 = matrix[r1][(col1 + 1) % 5]
            e2 = matrix[r2][(col2 + 1) % 5]
            rule = f"Same Row {r1} -> Shift Right"
        elif col1 == col2:
            e1 = matrix[(r1 + 1) % 5][col1]
            e2 = matrix[(r2 + 1) % 5][col2]
            rule = f"Same Col {col1} -> Shift Down"
        else:
            e1 = matrix[r1][col2]
            e2 = matrix[r2][col1]
            rule = f"Rectangle ({r1},{col1}) & ({r2},{col2}) -> Swap Cols"

        cipher_digrams.append(e1 + e2)
        print(f"  Step {idx:2d}: '{c1}{c2}' -> Rule: {rule:<35} -> Cipher: '{e1}{e2}'")

    final_ciphertext = "".join(cipher_digrams)
    print(f"\n--- Final Encrypted Result ---")
    print(f"Ciphertext: {final_ciphertext}")
    return final_ciphertext

def main():
    print("==================================================")
    print("      EXPERIMENT 10: PLAYFAIR ENCRYPTION TRACE   ")
    print("==================================================")

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        key = "PLAYFAIR EXAMPLE"
        plaintext = "HIDE THE GOLD IN THE TREE STUMP"
        print("[+] Demo Mode Activated")
    else:
        key = input("[+] Enter Key: ").strip()
        plaintext = input("[+] Enter Plaintext: ").strip()

    detailed_playfair_encrypt(plaintext, key)

    print("\n[OK] SUCCESS: Playfair Encryption Trace Execution Completed!")

if __name__ == "__main__":
    main()
