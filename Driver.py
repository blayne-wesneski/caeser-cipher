"""
A simple program that encrypts, decrypts, and cracks caeser (shift) ciphers
"""

# import modules
from Encrypt import encrypt
from Decrypt import decrypt
from Crack import crack

__author__ = "Blayne Wesneski"

type = input(
    """
             What function would you like to perform? 
             (1). Encrypt 
             (2). Decrypt 
             (3). Crack 
             
             """
)

if type == "1":
    plaintext = input("What is the plaintext you would like to encrypt? ")

    key = int(input("What is the key you would like to use? "))

    encrypt(plaintext, key)

elif type == "2":
    ciphertext = input("What is the ciphertext you would like to decrypt? ")

    key = int(input("What is the key for the ciphertext? "))

    decrypt(ciphertext, key)

elif type == "3":
    ciphertext = input("What is the ciphertext you would like to crack? ")

    crack(ciphertext)
