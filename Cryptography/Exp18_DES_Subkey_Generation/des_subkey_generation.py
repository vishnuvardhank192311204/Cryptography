# DES Subkey Generation Simulation (PC-1, Rotations, PC-2)
import binascii

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def simulate_subkey_gen():
    print("--- DES Subkey Generation Demonstration ---")
    
    # Dummy 56-bit key after PC-1 (represented as string of bits)
    # We use 28 bits of 0s and 1s for C and D for educational demonstration
    C = "0111111100000000111111110000"
    D = "1010101010101010101010101010"
    
    print(f"Initial C0 (28 bits): {C}")
    print(f"Initial D0 (28 bits): {D}\n")
    
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    # In PC-2, 24 bits are selected from C, and 24 bits from D
    # We'll just take the first 24 bits of each for this simulation
    
    for round_num in range(1, 17):
        s = shifts[round_num-1]
        C = left_shift(C, s)
        D = left_shift(D, s)
        
        # Subkey is 48 bits (24 from C + 24 from D) via PC-2
        subkey_C_part = C[:24]
        subkey_D_part = D[:24]
        K = subkey_C_part + subkey_D_part
        
        print(f"Round {round_num} (Shift {s}):")
        print(f"  C{round_num}: {C}")
        print(f"  D{round_num}: {D}")
        print(f"  Subkey K{round_num} (48 bits): {K}")
        print(f"  -> Origin: First 24 bits from C subset, next 24 bits from D subset.\n")

if __name__ == "__main__":
    simulate_subkey_gen()
