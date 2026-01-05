from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import requests
import os


def read_file(filepath):
    with open(filepath, "rb") as file:  # What mode for reading binary?
        contents = file.read()  # Read doesn't need parameters
        return contents  # What should we return?

def write_file(filepath, data):
    with open(filepath, "wb") as file:  
        file.write(data)  

# key = Fernet.generate_key() generates a random key

def generate_key_from_password(password):
    # Convert password string to bytes
    password_bytes = password.encode()
    
    # We need something called a "salt" - I'll explain this in a moment
    salt = b'some_salt_value_12345'  # This is a fixed value for now
    
    # Create a key derivation function
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    # Derive the key from the password
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key

def encrypt_file(filepath, password):
    # Step 1: Generate key from password
    key = generate_key_from_password(password)
    
    # Step 2: Create a Fernet object (this is what does the actual encryption)
    fernet = Fernet(key)
    
    # Step 3: Read the original file
    original_data = read_file(filepath)
    
    # Step 4: Encrypt the data
    encrypted_data = fernet.encrypt(original_data)
    
    # Step 5: Write encrypted data to a new file
    encrypted_filepath = filepath + ".encrypted"
    write_file(encrypted_filepath, encrypted_data)
    
    print(f"File encrypted successfully! Saved as: {encrypted_filepath}")

def decrypt_file(filepath, password):
    # Step 1: Generate key from password
    key = generate_key_from_password(password)
    
    # Step 2: Create a Fernet object (this is what does the actual encryption)
    fernet = Fernet(key)
    
    # Step 3: Read the scambled file
    scambled_data = read_file(filepath)
    
    # Step 4: Decrypt the data
    decrypted_data = fernet.decrypt(scambled_data)
    
    # Step 5: Write decrpyted data to a new file
    decrypted_filepath = filepath.replace(".encrypted", "")
    write_file(decrypted_filepath, decrypted_data)
    
    print(f"File Decrpyed successfully! Saved as: {decrypted_filepath}")

def main():
    user_choice =int(input("Enter 1:encrypt or 2:decrypt? "))
    password = input("What is your password? ")
    filepath = input("What is teh path of your file? ")

    if user_choice == 1:
        encrypt_file(filepath, password)
    elif user_choice == 2:
        decrypt_file(filepath, password)
    else:
        print("incorrect input please try again")

    del_file = input("would you liek to delete the file yes/y/no/n? ")
    if del_file.lower() in ["yes", "y"]:
        os.remove(filepath)
        print("file successfully deleteed!")
    else:
        print("Ok, no deletion needed!")

main()