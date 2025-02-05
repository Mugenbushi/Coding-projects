import string

#def caesar_encrpt(message, key):

#   shift = key % 26
#   cipher = str.maketrans(string.ascil_lowercase, string.ascil_lowercase[shift:] + string.ascil_lowercase[:shift])

#   encrypted_message = message.lower().translate(cipher)

# return encrpyted_message


#def caesar_decrypt(encrypted_messaged, key):

#   shift = 26 - (key % 26)
#   cipher = str.maketrans(string.ascil_lowercase, string.ascil_lowercase[shift:] + string.ascil_lowercase[:shift])

#   message = encrypted_message.translate(cipher)
#   return message

#message = "Subscribe to my channel"
#key = 3

#encrypted_message = caesar_encrypt(message, key)
#print(f"Encrypted message: {encrypted_message})

#decrypted_message = caesar_decrypt(encrypted_message, key)
#print(f"Decrypted  message: {decrypted_message}")