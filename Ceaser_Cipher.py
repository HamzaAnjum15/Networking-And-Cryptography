def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            ascii_code = ord(char.lower())
            shifted_ascii_code = (ascii_code - 97 + shift) % 26 + 97
            shifted_char = chr(shifted_ascii_code)
            result += shifted_char.upper() if is_upper else shifted_char
        else:
            result += char
    return result

text = input("Enter Text: ")
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)
