"""
Experiment 9: Playfair Cipher Case Study - PT-109 Message Decryption
----------------------------------------------------------------------
Historical Context:
On August 2, 1943, Lieutenant John F. Kennedy's patrol torpedo boat PT-109 was 
rammed and sunk by Japanese destroyer Amagiri. Australian coastwatcher Reginald Evans 
spotted the explosion and transmitted an encrypted Playfair cipher message:

Key: "ROYAL NEW ZEALAND NAVY"
Ciphertext: KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI SZXBY FOYBN BBNSP BWBUS WBTYX USBQX UDBNC ABAOP WZWFB YAYAX UEFOU YAZBA
"""

import sys

def build_playfair_matrix(key: str):
    """Builds 5x5 Playfair grid with J replaced by I."""
    key_clean = []
    seen = set()
    for char in key.upper():
        if char == 'J':
            char = 'I'
        if char.isalpha() and char not in seen:
            seen.add(char)
            key_clean.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            key_clean.append(char)

    matrix = [key_clean[i:i+5] for i in range(0, 25, 5)]
    pos_map = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    return matrix, pos_map

def decrypt_pt109(ciphertext: str, key: str) -> str:
    """Decrypts PT-109 Playfair message."""
    matrix, pos_map = build_playfair_matrix(key)
    clean_c = [('I' if c == 'J' else c) for c in ciphertext.upper() if c.isalpha()]
    
    # Pad with 'X' if odd length (shouldn't happen in valid Playfair but handle gracefully)
    if len(clean_c) % 2 != 0:
        clean_c.append('X')

    plaintext_chars = []
    for i in range(0, len(clean_c), 2):
        c1, c2 = clean_c[i], clean_c[i+1]
        r1, col1 = pos_map[c1]
        r2, col2 = pos_map[c2]

        if r1 == r2: # Same row
            p1 = matrix[r1][(col1 - 1) % 5]
            p2 = matrix[r2][(col2 - 1) % 5]
        elif col1 == col2: # Same column
            p1 = matrix[(r1 - 1) % 5][col1]
            p2 = matrix[(r2 - 1) % 5][col2]
        else: # Rectangle
            p1 = matrix[r1][col2]
            p2 = matrix[r2][col1]
        plaintext_chars.append(p1 + p2)

    return "".join(plaintext_chars)

def main():
    print("==================================================")
    print("  EXPERIMENT 9: HISTORICAL PT-109 PLAYFAIR DECRYPT")
    print("==================================================")

    historical_key = "ROYAL NEW ZEALAND NAVY"
    historical_cipher = (
        "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY "
        "CAJPO BOTEI SZXBY FOYBN BBNSP BWBUS WBTYX USBQX UDBNC "
        "ABAOP WZWFB YAYAX UEFOU YAZBA"
    )

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        key = historical_key
        ciphertext = historical_cipher
        print("[+] Demo Mode Activated")
    else:
        key_in = input(f"[+] Key (default='{historical_key}'): ").strip()
        key = key_in if key_in else historical_key
        cipher_in = input("[+] Enter PT-109 Ciphertext (press enter for default PT-109 text): ").strip()
        ciphertext = cipher_in if cipher_in else historical_cipher

    matrix, _ = build_playfair_matrix(key)

    print(f"\n--- Historical Key Matrix ('{key}') ---")
    for row in matrix:
        print("  ".join(row))

    print(f"\n--- PT-109 Encrypted Message ---")
    print(f"{ciphertext}")

    decrypted_text = decrypt_pt109(ciphertext, key)

    print(f"\n--- Decrypted Historical Message ---")
    print(f"Decrypted Raw Output: {decrypted_text}")

    print("\n[OK] SUCCESS: PT-109 Playfair Decryption Completed!")

if __name__ == "__main__":
    main()
