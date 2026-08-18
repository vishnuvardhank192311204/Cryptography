def rsa_small_message_demo():
    print("--- RSA Individual Character Encryption Vulnerability ---")
    
    # Large RSA parameters
    n = 3233  # Just an educational example (61 * 53)
    e = 17
    
    print(f"Modulus n = {n}, Public e = {e}")
    print("Mapping: A=0, B=1, ..., Z=25")
    
    message = "HELLO"
    print(f"\nEncrypting message: {message}")
    
    ciphertexts = []
    for char in message:
        m = ord(char) - ord('A')
        c = pow(m, e, n)
        ciphertexts.append(c)
        print(f"   '{char}' (m={m:2d}) -> Encrypted: {c}")
        
    print(f"\nCiphertext Stream: {ciphertexts}")
    
    print("\nVulnerability Analysis:")
    print("1. Same plaintext character always produces the same ciphertext.")
    print("   (Notice how both 'L's encrypted to the exact same value).")
    print("2. The plaintext space is incredibly small (only 26 possible values).")
    
    print("\nAttack Strategy (Codebook/Enumeration):")
    print("An attacker knows 'e' and 'n'. They simply encrypt the numbers 0 through 25")
    print("themselves and build a lookup table mapping ciphertext -> plaintext.")
    print("Then they look up the intercepted ciphertexts in their table to decrypt the")
    print("message instantly without ever knowing the private key 'd'.")
    print("This is why textbook RSA requires proper padding (like OAEP) to ensure")
    print("randomness and a large message space.")

if __name__ == "__main__":
    rsa_small_message_demo()
