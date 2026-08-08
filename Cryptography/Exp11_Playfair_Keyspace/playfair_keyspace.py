"""
Experiment 11: Playfair Cipher Keyspace Analysis
-------------------------------------------------
Algorithm & Mathematical Foundations:
1. Matrix Size: 5x5 grid containing 25 distinct letters (I and J merged).
2. Total Theoretical Key Permutations:
   Total = 25! = 15,511,210,043,330,985,984,000,000 (~1.55 x 10^25)
3. Cyclic Shift Equivalence:
   - Shifting all rows down by 1 position (5 cyclic row shifts) produces identical digram relationships.
   - Shifting all columns right by 1 position (5 cyclic column shifts) produces identical digram relationships.
   - Total identical shift configurations per matrix = 5 x 5 = 25.
4. Effective Keyspace:
   Effective Keys = 25! / 25 = 24! ≈ 6.204484 x 10^23 keys.
5. Bit Strength Equivalence:
   log2(24!) ≈ 79.08 bits of cryptographic key security.
"""

import sys
import math

def calculate_playfair_keyspace():
    """Computes exact integer and scientific notation keyspace bounds."""
    total_permutations = math.factorial(25)
    cyclic_equivalents = 25
    effective_keyspace = math.factorial(24)
    bit_security = math.log2(effective_keyspace)

    return total_permutations, cyclic_equivalents, effective_keyspace, bit_security

def main():
    print("==================================================")
    print("      EXPERIMENT 11: PLAYFAIR KEYSPACE ANALYSIS   ")
    print("==================================================")

    total_perm, equiv, effective_keys, bits = calculate_playfair_keyspace()

    print(f"\n--- Mathematical Keyspace Computations ---")
    print(f"1. Grid Dimensions           : 5 x 5 (25 Alphabet Cells, 'I' & 'J' Combined)")
    print(f"2. Total Key Permutations    : 25! = {total_perm:,}")
    print(f"   (Scientific Notation)     : {total_perm:.6e}")
    print(f"3. Cyclic Shift Equivalence  : 5 Row Shifts x 5 Col Shifts = {equiv} Equivalent Grids")
    print(f"4. Effective Unique Keyspace : 25! / 25 = 24! = {effective_keys:,}")
    print(f"   (Scientific Notation)     : {effective_keys:.6e}")
    print(f"5. Key Security Strength     : ~{bits:.2f} bits of entropy")

    print(f"\n--- Brute Force Security Evaluation ---")
    attempts_per_sec = 10**12 # 1 Trillion keys / sec
    seconds = effective_keys / attempts_per_sec
    years = seconds / (365.25 * 86400)
    print(f"At 1 Trillion keys/sec brute force speed:")
    print(f"  Time to exhaust effective keyspace: {years:.2e} years")

    print("\n[OK] SUCCESS: Playfair Keyspace Calculation & Analysis Completed!")

if __name__ == "__main__":
    main()
