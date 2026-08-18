import math

def rsa_common_factor_demo():
    print("--- RSA Common Factor Attack Demonstration ---")
    
    # Educational small primes
    p = 61
    q = 53
    n = p * q
    print(f"Given Modulus: n = {n}")
    
    # Let plaintext m share a factor with n.
    # Suppose m happens to be a multiple of p.
    m = p * 2 
    print(f"Plaintext m = {m}")
    
    print("\nAttacker knows 'm' and 'n'. Attacker computes gcd(m, n):")
    shared_factor = math.gcd(m, n)
    print(f"gcd({m}, {n}) = {shared_factor}")
    
    if shared_factor > 1 and shared_factor != n:
        print(f"-> A prime factor of n is revealed: {shared_factor}")
        other_factor = n // shared_factor
        print(f"-> The other prime factor is: {other_factor}")
        print("\nWhy does this compromise RSA?")
        print("RSA's security relies entirely on the difficulty of factoring 'n'.")
        print("If an attacker finds a plaintext (or even ciphertext) that shares a common")
        print("factor with 'n', they can use the extremely fast Euclidean algorithm (gcd)")
        print("to instantly factor 'n', breaking the private key completely.")
    else:
        print("No non-trivial common factor.")

if __name__ == "__main__":
    rsa_common_factor_demo()
