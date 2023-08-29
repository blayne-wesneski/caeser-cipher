def encrypt(plaintext, key):
    # intialize result variable
    result = ""

    # create for loop to loop through text
    for i in range(len(plaintext)):
        char = plaintext[i]

        # check for a space
        if char == " ":
            result += " "

        # encrypt uppercase characters
        elif char.isupper():
            result += chr(((ord(char)) + key - 65) % 26 + 65)

        # encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    # print results

    print("The encrypted message is: " + result)
    print("The original plaintext is: " + plaintext)
    print("The key is: " + str(key))
