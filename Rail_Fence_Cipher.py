def encrypt_rail_fence(plaintext, rails):
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in plaintext:
        fence[rail][rail] = char
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    ciphertext = ''.join(char for row in fence for char in row if char)
    return ciphertext

def decrypt_rail_fence(ciphertext, rails):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    rail = 0
    direction = 1
    idx = 0
    
    for _ in range(len(ciphertext)):
        fence[rail][_] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    for rail in range(rails):
        for col in range(len(ciphertext)):
            if fence[rail][col] == '*':
                fence[rail][col] = ciphertext[idx]
                idx += 1
                rail += direction
                if rail == rails - 1 or rail == 0:
                    direction = -direction
    
    plaintext = ''
    rail = 0
    direction = 1
    for _ in range(len(ciphertext)):
        plaintext += fence[rail][_]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    return plaintext

# Example usage:
plaintext = "Hamza Anjum"
rails = 3

encrypted_text = encrypt_rail_fence(plaintext, rails)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt_rail_fence(encrypted_text, rails)
print("Decrypted:", decrypted_text)
