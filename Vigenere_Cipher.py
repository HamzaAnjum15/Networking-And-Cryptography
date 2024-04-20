def encrypt_vigenere(plain_text, keyword):
    plain_text = plain_text.upper()
    keyword = keyword.upper()
    
    encrypted_text = ''
    keyword_index = 0
    
    for char in plain_text:
        if char.isalpha():  
            shift = ord(keyword[keyword_index]) - ord('A')
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            encrypted_text += char  
    
    return encrypted_text

def decrypt_vigenere(encrypted_text, keyword):
    encrypted_text = encrypted_text.upper()
    keyword = keyword.upper()
    
    decrypted_text = ''
    keyword_index = 0
    
    for char in encrypted_text:
        if char.isalpha():  
            shift = ord(keyword[keyword_index]) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += decrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            decrypted_text += char  
    
    return decrypted_text

plain_text = "HELLO"
keyword = "KEY"
encrypted_text = encrypt_vigenere(plain_text, keyword)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt_vigenere(encrypted_text, keyword)
print("Decrypted text:", decrypted_text)
