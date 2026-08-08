def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def encrypt(text, a, b):
    cipher = ""

    for ch in text:
        if ch.isupper():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            cipher += chr(c + ord('A'))

        elif ch.islower():
            p = ord(ch) - ord('a')
            c = (a * p + b) % 26
            cipher += chr(c + ord('a'))

        else:
            cipher += ch

    return cipher


def decrypt(cipher, a, b):
    plain = ""
    a_inv = mod_inverse(a, 26)

    if a_inv is None:
        return "Decryption not possible because 'a' has no modular inverse."

    for ch in cipher:
        if ch.isupper():
            c = ord(ch) - ord('A')
            p = (a_inv * (c - b)) % 26
            plain += chr(p + ord('A'))

        elif ch.islower():
            c = ord(ch) - ord('a')
            p = (a_inv * (c - b)) % 26
            plain += chr(p + ord('a'))

        else:
            plain += ch

    return plain


text = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if mod_inverse(a, 26) is None:
    print("Invalid value of a. Choose a value coprime with 26.")
else:
    cipher = encrypt(text, a, b)
    print("Encrypted Text :", cipher)

    plain = decrypt(cipher, a, b)
    print("Decrypted Text :", plain)