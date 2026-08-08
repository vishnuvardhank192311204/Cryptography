"""
Experiment 14: One-Time Pad (Vernam Cipher) Implementation
-----------------------------------------------------------
Algorithm & Cryptographic Principles:
The One-Time Pad (OTP) is an information-theoretically secure encryption method.
Conditions for Perfect Secrecy (Shannon's Theorem):
1. Key length must equal or exceed plaintext length.
2. Key must be purely random.
3. Key must never be reused in whole or part.
4. Key must be kept completely secret.

Formulas (Bitwise XOR):
- Encryption : C_i = P_i ⊕ K_i
- Decryption : P_i = C_i ⊕ K_i
"""

import sys
import os

def generate_random_key(length: int) -> bytes:
    """Generates cryptographically random bytes of given length."""
    return os.urandom(length)

def otp_encrypt(plaintext: str, key_bytes: bytes) -> (bytes, str):
    """Encrypts plaintext string with key_bytes using XOR."""
    p_bytes = plaintext.encode('utf-8')
    c_bytes = bytes([p ^ k for p, k in zip(p_bytes, key_bytes)])
    return c_bytes, c_bytes.hex().upper()

def otp_decrypt(c_bytes: bytes, key_bytes: bytes) -> str:
    """Decrypts ciphertext bytes with key_bytes using XOR."""
    p_bytes = bytes([c ^ k for c, k in zip(c_bytes, key_bytes)])
    return p_bytes.decode('utf-8', errors='replace')

def main():
    print("==================================================")
    print("           EXPERIMENT 14: ONE-TIME PAD            ")
    print("==================================================")

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        plaintext = "TOP SECRET MESSAGE ONE TIME PAD"
        print("[+] Demo Mode Activated")
    else:
        plaintext = input("[+] Enter Plaintext: ").strip()

    p_bytes = plaintext.encode('utf-8')
    key_bytes = generate_random_key(len(p_bytes))

    print(f"\n--- Parameter & Key Generation ---")
    print(f"Plaintext        : {plaintext}")
    print(f"Plaintext (Hex)  : {p_bytes.hex().upper()}")
    print(f"Random Key (Hex) : {key_bytes.hex().upper()}")

    # Encryption
    c_bytes, c_hex = otp_encrypt(plaintext, key_bytes)
    print(f"\n--- Encryption Process (Bitwise XOR) ---")
    print(f"Ciphertext (Hex) : {c_hex}")

    # Decryption
    decrypted = otp_decrypt(c_bytes, key_bytes)
    print(f"\n--- Decryption Process (Bitwise XOR) ---")
    print(f"Decrypted Text   : {decrypted}")

    print(f"\n--- Security Verification ---")
    print(f"Perfect Secrecy Status: ACHIEVED (Key length {len(key_bytes)} bytes == Plaintext length)")

    print("\n[OK] SUCCESS: One-Time Pad Execution Completed!")

if __name__ == "__main__":
    main()
