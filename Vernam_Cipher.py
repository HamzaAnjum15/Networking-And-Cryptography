def vernam_encrypt(message, key):
    message_binary = ''.join(format(ord(char), '08b') for char in message)
    key_binary = ''.join(format(ord(char), '08b') for char in key)
    
    encrypted_binary = ''.join(str(int(message_bit) ^ int(key_bit)) for message_bit, key_bit in zip(message_binary, key_binary))
    
    encrypted_message = ''.join(chr(int(encrypted_binary[i:i+8], 2)) for i in range(0, len(encrypted_binary), 8))
    
    return encrypted_message

def vernam_decrypt(encrypted_message, key):
    encrypted_binary = ''.join(format(ord(char), '08b') for char in encrypted_message)
    key_binary = ''.join(format(ord(char), '08b') for char in key)
    
    decrypted_binary = ''.join(str(int(encrypted_bit) ^ int(key_bit)) for encrypted_bit, key_bit in zip(encrypted_binary, key_binary))
    
    decrypted_message = ''.join(chr(int(decrypted_binary[i:i+8], 2)) for i in range(0, len(decrypted_binary), 8))
    
    return decrypted_message

message = "HELLO"
key = "UBITCS"
encrypted_message = vernam_encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = vernam_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
