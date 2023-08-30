"""
A simple program that encrypts, decrypts, and cracks Caesar (shift) ciphers
"""

# Import necessary modules
from Encrypt import encrypt
from Decrypt import decrypt
from Crack import crack

__author__ = "Blayne Wesneski"

# Ask the user to choose a function (Encrypt, Decrypt, or Crack)
type = input(
            """
             What function would you like to perform? 
             (1). Encrypt 
             (2). Decrypt 
             (3). Crack 
             
             """
)

# If the user chooses to Encrypt
if type == "1":
    plaintext = input("What is the plaintext you would like to encrypt? ")
    key = int(input("What is the key you would like to use? "))
    encrypt(plaintext, key)  # Call the encrypt function

# If the user chooses to Decrypt
elif type == "2":
    ciphertext = input("What is the ciphertext you would like to decrypt? ")
    key = int(input("What is the key for the ciphertext? "))
    decrypt(ciphertext, key)  # Call the decrypt function

# If the user chooses to Crack
elif type == "3":
    ciphertext = input("What is the ciphertext you would like to crack? ")
    crack(ciphertext)  # Call the crack function
