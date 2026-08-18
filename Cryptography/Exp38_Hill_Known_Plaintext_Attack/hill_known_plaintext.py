import math

def mod_inverse_matrix_2x2(matrix, mod):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod
    # Find mod inverse of det
    det_inv = -1
    for i in range(mod):
        if (det * i) % mod == 1:
            det_inv = i
            break
    if det_inv == -1:
        return None # Not invertible
        
    adj = [
        [matrix[1][1], -matrix[0][1]],
        [-matrix[1][0], matrix[0][0]]
    ]
    
    inv = [
        [(adj[0][0] * det_inv) % mod, (adj[0][1] * det_inv) % mod],
        [(adj[1][0] * det_inv) % mod, (adj[1][1] * det_inv) % mod]
    ]
    return inv

def multiply_matrices(A, B, mod):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            C[i][j] = (A[i][0] * B[0][j] + A[i][1] * B[1][j]) % mod
    return C

def hill_kpa():
    print("--- Hill Cipher Known Plaintext Attack (2x2) ---")
    
    # C = K * P mod 26
    # We want K = C * P^-1 mod 26
    
    # Let's say we intercepted this known plaintext-ciphertext pair (2 blocks = 4 chars)
    # P = "HELP" -> H=7, E=4, L=11, P=15
    # C = "HIAT" -> H=7, I=8, A=0, T=19
    
    P_matrix = [[7, 11], [4, 15]] # Columns: [H, E]^T and [L, P]^T
    C_matrix = [[7, 0], [8, 19]]  # Columns: [H, I]^T and [A, T]^T
    
    print("Known Plaintext Matrix (Columns = Blocks):")
    for row in P_matrix: print(row)
        
    print("\nKnown Ciphertext Matrix:")
    for row in C_matrix: print(row)
        
    print("\nCalculating P^-1 mod 26...")
    P_inv = mod_inverse_matrix_2x2(P_matrix, 26)
    
    if P_inv is None:
        print("The plaintext matrix is not invertible modulo 26. Attack fails.")
        print("To succeed, the determinant of P must be relatively prime to 26.")
        return
        
    print("P^-1 Matrix:")
    for row in P_inv: print(row)
        
    print("\nCalculating K = C * P^-1 mod 26...")
    K = multiply_matrices(C_matrix, P_inv, 26)
    
    print("\nRecovered Key Matrix K:")
    for row in K: print(row)
        
    print("\nVerification:")
    print("To verify, if we encrypt 'HE' (7, 4) with this K:")
    C1 = (K[0][0]*7 + K[0][1]*4) % 26
    C2 = (K[1][0]*7 + K[1][1]*4) % 26
    print(f"C = ({C1}, {C2}) -> {chr(C1+65)}{chr(C2+65)}. Matches 'HI' (7, 8).")

if __name__ == "__main__":
    hill_kpa()
