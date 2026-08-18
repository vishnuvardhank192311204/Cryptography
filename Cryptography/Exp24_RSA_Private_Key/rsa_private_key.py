def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def mod_inverse(e, phi):
    gcd_val, x, y = extended_gcd(e, phi)
    if gcd_val != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def find_prime_factors(n):
    # Simple trial division for small numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def rsa_private_key_demo():
    print("--- RSA Private Key Recovery ---")
    e = 31
    n = 3599
    print(f"Given Public Key: e={e}, n={n}")
    
    p, q = find_prime_factors(n)
    print(f"1. Trial division factors of n: p={p}, q={q}")
    
    if not p or not q:
        print("Failed to factorize.")
        return
        
    phi = (p - 1) * (q - 1)
    print(f"2. Computed φ(n) = (p-1)*(q-1) = {phi}")
    
    d = mod_inverse(e, phi)
    print(f"3. Private key d = e^(-1) mod φ(n) = {d}")

if __name__ == "__main__":
    rsa_private_key_demo()
