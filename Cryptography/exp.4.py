def encrypt(plaintext, key):
    cipher_text = ""
    key = key.upper()
    key_index = 0

    for ch in plaintext:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if ch.isupper():
                encrypted_char = chr(
                    (ord(ch) - ord('A') + shift) % 26 + ord('A')
                )
            else:
                encrypted_char = chr(
                    (ord(ch) - ord('a') + shift) % 26 + ord('a')
                )

            cipher_text += encrypted_char
            key_index += 1
        else:
            cipher_text += ch

    return cipher_text


def decrypt(cipher_text, key):
    plaintext = ""
    key = key.upper()
    key_index = 0

    for ch in cipher_text:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if ch.isupper():
                decrypted_char = chr(
                    (ord(ch) - ord('A') - shift) % 26 + ord('A')
                )
            else:
                decrypted_char = chr(
                    (ord(ch) - ord('a') - shift) % 26 + ord('a')
                )

            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += ch

    return plaintext


text = input("Enter the plaintext: ")
key = input("Enter the key: ")

if not key.isalpha():
    print("The key must contain alphabet letters only.")
else:
    encrypted_text = encrypt(text, key)
    decrypted_text = decrypt(encrypted_text, key)

    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)