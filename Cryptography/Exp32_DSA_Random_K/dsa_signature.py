import random
import hashlib

def mod_inverse(a, m):
    # Extended Euclidean
    m0 = m
    y = 0
    x = 1
    if m == 1: return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0: x = x + m0
    return x

def dsa_demo():
    print("--- DSA Random 'k' Demonstration ---")
    # Small prime parameters for educational demo
    p = 23
    q = 11  # q divides p-1 (22)
    h = 2   # h^((p-1)/q) mod p
    g = pow(h, (p-1)//q, p)
    
    print(f"Public Params: p={p}, q={q}, g={g}")
    
    # Private Key
    x = 7
    # Public Key
    y = pow(g, x, p)
    print(f"Private Key (x): {x}")
    print(f"Public Key (y): {y}")
    
    msg = "HELLO"
    H_m = int(hashlib.sha1(msg.encode()).hexdigest(), 16) % q
    
    print(f"\nMessage: {msg}")
    print(f"Message Hash (mod q): {H_m}")
    
    print("\n--- Signature 1 ---")
    k1 = 3 # Random nonce 1
    r1 = pow(g, k1, p) % q
    s1 = (mod_inverse(k1, q) * (H_m + x * r1)) % q
    print(f"Using random k={k1} -> Signature: (r={r1}, s={s1})")
    
    print("\n--- Signature 2 ---")
    k2 = 5 # Random nonce 2
    r2 = pow(g, k2, p) % q
    s2 = (mod_inverse(k2, q) * (H_m + x * r2)) % q
    print(f"Using random k={k2} -> Signature: (r={r2}, s={s2})")
    
    print("\n--- Verification ---")
    def verify(r, s):
        if r <= 0 or r >= q or s <= 0 or s >= q: return False
        w = mod_inverse(s, q)
        u1 = (H_m * w) % q
        u2 = (r * w) % q
        v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
        return v == r
        
    print(f"Verify Sig 1: {verify(r1, s1)}")
    print(f"Verify Sig 2: {verify(r2, s2)}")
    
    print("\nExplanation:")
    print("Unlike textbook RSA which is deterministic (encrypting the same message yields the")
    print("same signature), DSA inherently requires a randomly generated 'k' for EVERY signature.")
    print("Because 'k' changes, the resulting signature (r,s) differs completely even for the exact")
    print("same message and private key. If an attacker discovers that two signatures used the same 'k',")
    print("they can easily recover the private key 'x'. Therefore, 'k' MUST be randomly generated.")

if __name__ == "__main__":
    dsa_demo()
