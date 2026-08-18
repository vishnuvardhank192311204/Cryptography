def diffie_hellman_demo():
    print("--- Diffie-Hellman Key Exchange Demonstration ---")
    
    # Public parameters
    q = 23 # Prime modulus
    a = 5  # Generator
    print(f"Public parameters: Modulus q = {q}, Generator a = {a}")
    
    # Secret numbers
    x = 4 # Alice's secret
    y = 3 # Bob's secret
    print(f"Alice's secret x = {x}")
    print(f"Bob's secret y = {y}")
    
    print("\n1. Standard Correct DH Construction:")
    A = pow(a, x, q)
    B = pow(a, y, q)
    print(f"   Alice sends A = a^x mod q = 5^4 mod 23 = {A}")
    print(f"   Bob sends B = a^y mod q = 5^3 mod 23 = {B}")
    
    K_Alice = pow(B, x, q)
    K_Bob = pow(A, y, q)
    print(f"   Alice computes K = B^x mod q = {B}^4 mod 23 = {K_Alice}")
    print(f"   Bob computes K = A^y mod q = {A}^3 mod 23 = {K_Bob}")
    print("   -> Success: Both share the same key.")
    
    print("\n2. Vulnerable/Incorrect Construction (x^a instead of a^x):")
    A_bad = pow(x, a, q)
    B_bad = pow(y, a, q)
    print(f"   Alice sends A_bad = x^a mod q = 4^5 mod 23 = {A_bad}")
    print(f"   Bob sends B_bad = y^a mod q = 3^5 mod 23 = {B_bad}")
    
    print("\n   What happens?")
    print("   Alice and Bob cannot compute a shared key this way.")
    print("   Alice has A_bad, Bob's B_bad, and her x. She cannot easily combine them.")
    
    print("\n   Can Eve break it?")
    print("   Yes! Eve sees A_bad (which is x^a mod q) and knows 'a' and 'q'.")
    print("   This is taking the a-th root modulo q.")
    print("   Since 'a' is known, computing the modular root is much easier than solving")
    print("   the Discrete Logarithm problem (which standard DH relies on).")
    print("   Eve can recover x and y directly.")

if __name__ == "__main__":
    diffie_hellman_demo()
