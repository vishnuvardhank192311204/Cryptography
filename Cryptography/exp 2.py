# Monoalphabetic Substitution Cipher

plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

plaintext = input("Enter the plaintext: ").upper()

ciphertext = ""

for ch in plaintext:
    if ch in plain_alphabet:
        index = plain_alphabet.index(ch)
        ciphertext += cipher_alphabet[index]
    else:
        ciphertext += ch

print("Cipher Text:", ciphertext)