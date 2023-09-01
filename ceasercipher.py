def caesar_cipher_encipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            encrypted_char_code = (char_code + shift) % 26
            encrypted_char = chr(encrypted_char_code + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_cipher_decipher(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            decrypted_char_code = (char_code - shift) % 26
            decrypted_char = chr(decrypted_char_code + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

while True:
    user_input = input("Enter text (or 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    operation = input("Choose operation (encode or decode): ").lower()
    
    if operation == 'encode':
        shift_amount = int(input("Enter shift amount (integer): "))
        encoded_text = caesar_cipher_encipher(user_input, shift_amount)
        print("Encoded Text:", encoded_text)
    elif operation == 'decode':
        shift_amount = int(input("Enter shift amount (integer): "))
        decoded_text = caesar_cipher_decipher(user_input, shift_amount)
        print("Decoded Text:", decoded_text)
    else:
        print("Invalid operation. Please choose 'encode' or 'decode'.")
