from Crypto.Cipher import DES
import binascii

def des_demo():
    print("--- DES Implementation Demonstration ---")
    print("Note: DES is obsolete and provided only for educational purposes.")
    print("It uses a 64-bit block size and a 56-bit effective key.")
    
    # 8-byte key (64 bits, but 8 bits are parity)
    key = b'8byteKey'
    print(f"\nKey: {key}")
    print(f"Key (Hex): {binascii.hexlify(key).decode()}")
    
    # 64-bit plaintext
    plaintext = b'12345678'
    print(f"\nPlaintext: {plaintext}")
    print(f"Plaintext (Hex): {binascii.hexlify(plaintext).decode()}")
    
    # Encrypt
    cipher_enc = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher_enc.encrypt(plaintext)
    
    print(f"\nCiphertext (Hex): {binascii.hexlify(ciphertext).decode()}")
    
    # Decrypt
    cipher_dec = DES.new(key, DES.MODE_ECB)
    decrypted = cipher_dec.decrypt(ciphertext)
    
    print(f"\nDecrypted: {decrypted}")
    
    if decrypted == plaintext:
        print("\nSuccess: Decrypted text matches original plaintext.")
    else:
        print("\nFailure: Decrypted text does not match.")
        
    print("\nInternals of DES:")
    print("1. Initial Permutation (IP) scrambles the 64-bit block.")
    print("2. Split into Left (32) and Right (32) halves.")
    print("3. 16 Feistel Rounds:")
    print("   a. Expansion Permutation (EP) expands Right to 48 bits.")
    print("   b. XOR with 48-bit round subkey.")
    print("   c. S-Box substitution (shrinks 48 bits back to 32 bits).")
    print("   d. P-Box permutation.")
    print("4. Final Permutation (IP^(-1)).")

if __name__ == "__main__":
    des_demo()
