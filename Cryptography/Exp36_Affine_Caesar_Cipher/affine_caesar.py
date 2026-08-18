import math

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_demo():
    print("--- Affine Cipher (aP + b mod 26) ---")
    
    a_input = input("Enter value for 'a': ")
    b_input = input("Enter value for 'b': ")
    
    try:
        a = int(a_input)
        b = int(b_input)
    except ValueError:
        print("Integers required.")
        return
        
    if math.gcd(a, 26) != 1:
        print(f"\nError: gcd({a}, 26) = {math.gcd(a, 26)}. 'a' must be relatively prime to 26.")
        
        print("\nDemonstration: Why a=2, b=3 is not one-to-one:")
        print("Let's encrypt P=0 (A) and P=13 (N) with a=2, b=3:")
        e_0 = (2 * 0 + 3) % 26
        e_13 = (2 * 13 + 3) % 26
        print(f"E(0) = (2*0 + 3) mod 26 = {e_0} -> 'D'")
        print(f"E(13) = (2*13 + 3) mod 26 = {e_13} -> 'D'")
        print("Two different plaintexts map to the SAME ciphertext.")
        print("Decryption is impossible because the modular inverse of 2 modulo 26 does not exist.")
        return
        
    plaintext = input("Enter plaintext to encrypt: ").upper()
    
    # Encrypt
    ct = ""
    for c in plaintext:
        if 'A' <= c <= 'Z':
            p = ord(c) - 65
            ct_val = (a * p + b) % 26
            ct += chr(ct_val + 65)
        else:
            ct += c
            
    print(f"Ciphertext: {ct}")
    
    # Decrypt
    a_inv = mod_inverse(a, 26)
    dec = ""
    for c in ct:
        if 'A' <= c <= 'Z':
            c_val = ord(c) - 65
            p_val = (a_inv * (c_val - b)) % 26
            dec += chr(p_val + 65)
        else:
            dec += c
            
    print(f"Decrypted: {dec}")

if __name__ == "__main__":
    affine_demo()
