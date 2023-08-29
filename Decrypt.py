def decrypt(ciphertext, key):
    result = ""

    # create for loop to loop through text
    for i in range(len(ciphertext)):
        char = ciphertext[i]

        # check for a space
        if char == " ":
            result += " "

        # decrypt uppercase characters
        elif char.isupper():
            result += chr(((ord(char)) - key - 65) % 26 + 65)

        # decrypt lowercase characters
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    print("The decrypted message is: " + result)
    print("The original ciphertext is: " + ciphertext)
    print("The key is: " + str(key))
