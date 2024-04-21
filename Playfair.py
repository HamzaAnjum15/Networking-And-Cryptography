def generate_playfair_matrix(key):
    # Remove duplicate letters from the key
    key = "".join(dict.fromkeys(key))
    # Fill the matrix with the key
    matrix = [list(key)]
    # Fill the remaining cells with the rest of the alphabet
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in key:
            matrix[-1].append(char)
            if len(matrix[-1]) == 5:
                matrix.append([])
    return matrix

def find_char(matrix, char):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    return None, None

def encrypt_pair(matrix, pair):
    char1, char2 = pair
    row1, col1 = find_char(matrix, char1)
    row2, col2 = find_char(matrix, char2)
    # Same row
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5], matrix[row2][(col2 + 1) % 5]
    # Same column
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1], matrix[(row2 + 1) % 5][col2]
    # Rectangle
    else:
        return matrix[row1][col2], matrix[row2][col1]

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    # Preprocess plaintext
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    # Encrypt pairs
    ciphertext = ""
    for pair in plaintext:
        encrypted_pair = encrypt_pair(matrix, pair)
        ciphertext += "".join(encrypted_pair)
    return ciphertext

# Example usage
plaintext = "HELLO WORLD"
key = "KEYWORD"
print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", playfair_encrypt(plaintext, key))
