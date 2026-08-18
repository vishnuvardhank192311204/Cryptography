def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

def dummy_encrypt(data, key):
    # Educational dummy block cipher: simple XOR for demonstration
    # Real CBC-MAC uses AES or DES.
    return xor_bytes(data, key)

def cbc_mac_forgery_demo():
    print("--- CBC-MAC Forgery Demonstration ---")
    
    key = b'K' * 8 # 8 byte key
    X = b'MESSAGE!' # 1 block message
    print(f"Original Message Block X: {X}")
    
    # Compute T = MAC(K, X)
    # Since it's 1 block, T = E(K, X)
    T = dummy_encrypt(X, key)
    print(f"Original Tag T: {T}")
    
    print("\nAdversary constructs two-block message: X || (X XOR T)")
    block2 = xor_bytes(X, T)
    print(f"Constructed Block 2: {block2}")
    
    # Let's compute CBC-MAC of this 2-block message
    # C1 = E(K, X) = T
    # C2 = E(K, C1 XOR block2) = E(K, T XOR (X XOR T)) = E(K, X) = T
    
    C1 = dummy_encrypt(X, key)
    C2_input = xor_bytes(C1, block2)
    C2 = dummy_encrypt(C2_input, key)
    
    new_T = C2
    print(f"New MAC Tag for the 2-block message: {new_T}")
    
    print("\nExplanation:")
    print("The new MAC perfectly matches the original MAC T!")
    print("In CBC-MAC, the chaining feeds the previous ciphertext (T) into the next block.")
    print("If the adversary provides Block2 = X XOR T, then during chaining:")
    print("   Input to E = Block2 XOR T = (X XOR T) XOR T = X")
    print("So the cipher evaluates E(K, X) again, resulting in T.")
    print("This allows an attacker to append arbitrary blocks and forge a valid MAC.")
    print("This is why plain CBC-MAC is only secure for fixed-length messages,")
    print("and algorithms like CMAC were invented to fix this.")

if __name__ == "__main__":
    cbc_mac_forgery_demo()
