def caesar_cipher(text, shift, mode='encrypt'): 
    if mode == 'decrypt': 
        shift = -shift 
    result = "" 
    for char in text: 
        if char.isalpha(): 
            shift_start = 65 if char.isupper() else 97 
            result += chr((ord(char) - shift_start + shift) % 26 + shift_start) 
        else: 
            result += char 
    return result 
 
# User input for operation 
operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ") 
 
# User input for message and shift value 
message = input("Enter your message: ") 
shift_value = int(input("Enter shift value: ")) 
 
# Encrypt or Decrypt 
output = caesar_cipher(message, shift_value, operation) 
print("Result:", output)