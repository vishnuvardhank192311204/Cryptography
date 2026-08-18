# Cryptography Lab Experiments

This repository contains the implementation of 40 Cryptography Lab experiments in Python 3.

## Experiments List
1. **Exp1_Caesar_Cipher**: Caesar Cipher encryption and decryption.
2. **Exp2_Monoalphabetic_Cipher**: Monoalphabetic Substitution Cipher.
3. **Exp3_Playfair_Cipher**: Playfair Cipher.
4. **Exp4_Vigenere_Cipher**: Vigenere Cipher.
5. **Exp5_Affine_Cipher**: Affine Cipher.
6. **Exp6_Affine_Cipher_Break**: Affine Cipher Break (Brute Force).
7. **Exp7_Substitution_Cipher_Decrypt**: Substitution Cipher Decrypt.
8. **Exp8_Keyword_Monoalphabetic**: Keyword Monoalphabetic Substitution.
9. **Exp9_Playfair_PT109**: Playfair Cipher PT-109 Decryption.
10. **Exp10_Playfair_Encryption**: Playfair Encryption using assignment matrix.
11. **Exp11_Playfair_Keyspace**: Calculate Playfair Keyspace.
12. **Exp12_Hill_Cipher**: Hill Cipher with key [9 4; 5 7].
13. **Exp13_Hill_Known_Plaintext**: Hill Known Plaintext Attack.
14. **Exp14_One_Time_Pad**: One Time Pad encryption/decryption.
15. **Exp15_Frequency_Attack**: Frequency Attack on Caesar Cipher.
16. **Exp16_Frequency_Attack**: Automatic frequency analysis attack against monoalphabetic substitution. (`python Exp16_Frequency_Attack/frequency_attack.py`)
17. **Exp17_DES_Decryption_Key_Generation**: DES decryption key generation and reverse shift schedule demonstration. (`python Exp17_DES_Decryption_Key_Generation/des_decryption.py`)
18. **Exp18_DES_Subkey_Generation**: DES subkey generation using PC-1, rotations, and PC-2. (`python Exp18_DES_Subkey_Generation/des_subkey_generation.py`)
19. **Exp19_CBC_3DES**: CBC encryption using 3DES (TDEA). (`python Exp19_CBC_3DES/cbc_3des.py`)
20. **Exp20_ECB_CBC_Error_Propagation**: Demonstration of ciphertext error propagation in ECB vs CBC modes. (`python Exp20_ECB_CBC_Error_Propagation/error_propagation.py`)
21. **Exp21_ECB_CBC_CFB_Padding**: Demonstration of padding for ECB, CBC, and CFB modes. (`python Exp21_ECB_CBC_CFB_Padding/padding_modes.py`)
22. **Exp22_CBC_SDES**: CBC encryption/decryption using Simplified DES (S-DES). (`python Exp22_CBC_SDES/cbc_sdes.py`)
23. **Exp23_CTR_SDES**: Counter (CTR) mode encryption/decryption using S-DES. (`python Exp23_CTR_SDES/ctr_sdes.py`)
24. **Exp24_RSA_Private_Key**: Finding RSA private key from public components using extended Euclidean algorithm. (`python Exp24_RSA_Private_Key/rsa_private_key.py`)
25. **Exp25_RSA_Common_Factor**: Demonstration of the RSA common factor attack. (`python Exp25_RSA_Common_Factor/rsa_common_factor.py`)
26. **Exp26_RSA_Key_Leak**: Analysis of RSA private key leak and modulus reuse implications. (`python Exp26_RSA_Key_Leak/rsa_key_leak.py`)
27. **Exp27_RSA_Small_Message_Attack**: Vulnerability of independent character encryption in textbook RSA. (`python Exp27_RSA_Small_Message_Attack/rsa_small_message_attack.py`)
28. **Exp28_Diffie_Hellman**: Diffie-Hellman key exchange and incorrect construction analysis. (`python Exp28_Diffie_Hellman/diffie_hellman.py`)
29. **Exp29_SHA3_Lane_Propagation**: SHA-3 state lane occupancy simulation and permutation analysis. (`python Exp29_SHA3_Lane_Propagation/sha3_lanes.py`)
30. **Exp30_CBC_MAC**: Demonstration of CBC-MAC extension/forgery concepts. (`python Exp30_CBC_MAC/cbc_mac.py`)
31. **Exp31_CMAC_Subkey_Generation**: CMAC subkey (K1, K2) generation via shift and conditional XOR. (`python Exp31_CMAC_Subkey_Generation/cmac_subkeys.py`)
32. **Exp32_DSA_Random_K**: Demonstration of DSA random nonce (k) usage vs deterministic RSA. (`python Exp32_DSA_Random_K/dsa_signature.py`)
33. **Exp33_DES**: Full DES algorithm implementation. (`python Exp33_DES/des.py`)
34. **Exp34_ECB_CBC_CFB**: Demonstrations of block modes ECB, CBC, and CFB padding. (`python Exp34_ECB_CBC_CFB/block_modes.py`)
35. **Exp35_One_Time_Pad_Vigenere**: Vigenère cipher operating as a one-time pad with random keystream. (`python Exp35_One_Time_Pad_Vigenere/otp_vigenere.py`)
36. **Exp36_Affine_Caesar_Cipher**: Affine Cipher (aP + b) and relatively prime modulus constraint demo. (`python Exp36_Affine_Caesar_Cipher/affine_caesar.py`)
37. **Exp37_Monoalphabetic_Frequency_Attack**: Improved automatic frequency attack using digrams. (`python Exp37_Monoalphabetic_Frequency_Attack/monoalphabetic_attack.py`)
38. **Exp38_Hill_Known_Plaintext_Attack**: Known plaintext attack on 2x2 Hill Cipher. (`python Exp38_Hill_Known_Plaintext_Attack/hill_known_plaintext.py`)
39. **Exp39_Additive_Cipher_Frequency_Attack**: Automatic frequency analysis and brute-force scoring against Additive/Caesar cipher. (`python Exp39_Additive_Cipher_Frequency_Attack/additive_frequency_attack.py`)
40. **Exp40_Monoalphabetic_Frequency_Attack_Advanced**: Stronger monoalphabetic attack simulating hill climbing. (`python Exp40_Monoalphabetic_Frequency_Attack_Advanced/advanced_frequency_attack.py`)

## Environment & Requirements
- **Python Version**: Python 3.x
- **Installation**: 
  ```bash
  pip install -r requirements.txt
  ```

## Output Screenshots
Due to environment limitations, if a terminal screenshot cannot be generated programmatically, a placeholder `output.png` and `screenshot_instructions.txt` are provided inside each directory. Run the scripts locally to capture actual execution screenshots for submission.

## Author
**VISHNU VARDHAN K**
