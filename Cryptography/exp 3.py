def create_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    letters = []

    for ch in keyword + alphabet:
        if ch.isalpha() and ch not in letters:
            letters.append(ch)

    matrix = []

    for i in range(0, 25, 5):
        matrix.append(letters[i:i + 5])

    return matrix


def find_position(matrix, letter):
    if letter == "J":
        letter = "I"

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col


def prepare_plaintext(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    pairs = []
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 < len(text):
            second = text[i + 1]

            if first == second:
                pairs.append(first + "X")
                i += 1
            else:
                pairs.append(first + second)
                i += 2
        else:
            pairs.append(first + "X")
            i += 1

    return pairs


def encrypt_pair(matrix, pair):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:
        return (
            matrix[row1][(col1 + 1) % 5]
            + matrix[row2][(col2 + 1) % 5]
        )

    elif col1 == col2:
        return (
            matrix[(row1 + 1) % 5][col1]
            + matrix[(row2 + 1) % 5][col2]
        )

    else:
        return matrix[row1][col2] + matrix[row2][col1]


keyword = input("Enter the keyword: ")
plaintext = input("Enter the plaintext: ")

matrix = create_matrix(keyword)
pairs = prepare_plaintext(plaintext)

ciphertext = ""

for pair in pairs:
    ciphertext += encrypt_pair(matrix, pair)

print("\nPlayfair Matrix:")

for row in matrix:
    print(" ".join(row))

print("\nPrepared pairs:", " ".join(pairs))
print("Cipher Text:", ciphertext)