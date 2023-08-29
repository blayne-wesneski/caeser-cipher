def crack(ciphertext):
    confirm = input(
        "This will list all possible shifts for you to choose the most likely candidate. Please enter [Y] to continue."
    )

    number = 0
    result = ""

    for x in range(1, 27):
        # create for loop to loop through text
        for i in range(len(ciphertext)):
            char = ciphertext[i]

            # check for a space
            if char == " ":
                result += " "

            # decrypt uppercase characters
            elif char.isupper():
                result += chr(((ord(char)) - x - 65) % 26 + 65)

            # decrypt lowercase characters
            else:
                result += chr((ord(char) - x - 97) % 26 + 97)

        number = number + 1
        print("Possible decryption #" + str(number) + " is:" + result)
        result = ""
