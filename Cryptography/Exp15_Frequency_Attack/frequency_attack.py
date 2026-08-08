"""
Experiment 15: Letter Frequency Analysis Attack Implementation
----------------------------------------------------------------
Algorithm & Cryptanalysis Concept:
In natural English text, letters occur with predictable relative frequencies.
Standard Relative Frequencies:
  'E': 12.7%, 'T': 9.1%, 'A': 8.2%, 'O': 7.5%, 'I': 7.0%, 'N': 6.7%,
  'S': 6.3%,  'H': 6.1%, 'R': 6.0%, 'D': 4.3%, 'L': 4.0%, 'U': 2.8%

Frequency Analysis Attack Steps:
1. Count frequency of each letter in ciphertext.
2. Rank ciphertext letters from highest to lowest frequency.
3. Predict shift key k = (Most Frequent Cipher Char - 'E') mod 26.
4. Output candidate decryptions for top likely shift keys.
"""

import sys
from collections import Counter

ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def get_ciphertext_frequencies(text: str) -> list:
    """Calculates frequency table sorted by occurrence."""
    clean = [c.upper() for c in text if c.isalpha()]
    total = len(clean)
    if total == 0:
        return []
    counts = Counter(clean)
    freqs = [(char, count, (count / total) * 100) for char, count in counts.most_common()]
    return freqs, total

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    res = []
    for char in ciphertext:
        if char.isupper():
            res.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        elif char.islower():
            res.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        else:
            res.append(char)
    return "".join(res)

def main():
    print("==================================================")
    print("      EXPERIMENT 15: FREQUENCY ANALYSIS ATTACK    ")
    print("==================================================")

    # Demo text encrypted with Caesar shift = 7
    # "CRYPTOGRAPHY IS THE PRACTICE AND STUDY OF TECHNIQUES FOR SECURE COMMUNICATION"
    # Encrypted shift 7: C->J, R->Y, Y->F, P->W, T->A, O->V, G->N, R->Y, A->H, P->W, H->O, Y->F
    sample_cipher = "JYFWAVNYHWOF PZ AOL WYHJAPJL HUK ZABKF VM ALJOUPXBLZ MVY ZLJBYL JVTTBUHJHPAPVU"

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        ciphertext = sample_cipher
        print("[+] Demo Mode Activated")
    else:
        ciphertext_in = input("[+] Enter Ciphertext: ").strip()
        ciphertext = ciphertext_in if ciphertext_in else sample_cipher

    freqs, total = get_ciphertext_frequencies(ciphertext)

    print(f"\n--- Ciphertext Frequency Analysis (Total Letters: {total}) ---")
    print(f"{'Char':<6}{'Count':<8}{'Percentage':<12}")
    print("-" * 26)
    for char, count, pct in freqs[:8]: # Display top 8
        print(f" '{char}'   {count:<8}{pct:.2f}%")

    if not freqs:
        print("[-] Ciphertext contains no alphabetic characters.")
        return

    most_frequent_char = freqs[0][0]
    predicted_shift = (ord(most_frequent_char) - ord('E')) % 26

    print(f"\n--- Predicted Key Derivation ---")
    print(f"Most Frequent Cipher Letter : '{most_frequent_char}'")
    print(f"Mapped to English 'E'        : Predicted Shift k = ({ord(most_frequent_char)} - {ord('E')}) mod 26 = {predicted_shift}")

    print(f"\n--- Top Candidate Decryptions ---")
    print(f"Candidate 1 (Shift={predicted_shift:2d}): {caesar_decrypt(ciphertext, predicted_shift)}")

    # Show top 3 candidates based on top cipher letters
    for i in range(1, min(4, len(freqs))):
        c = freqs[i][0]
        s = (ord(c) - ord('E')) % 26
        print(f"Candidate {i+1} (Shift={s:2d}): {caesar_decrypt(ciphertext, s)}")

    print("\n[OK] SUCCESS: Frequency Analysis Attack Execution Completed!")

if __name__ == "__main__":
    main()
