
text = input("Enter the plaintext: ")
k = int(input("Enter the key (1-25): "))

cipher = ""

for ch in text:
    if ch.isupper():
        cipher += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
    elif ch.islower():
        cipher += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    else:
        cipher += ch

print("Cipher Text:", cipher)