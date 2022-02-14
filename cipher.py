# ---------- cipher.py ----------
# A program to encode and decode
# messages with a one-time pad cipher
#
# Ben Carpenter
# February 9, 2022
# ---------- cipher.py ----------

from random import choice
import string
import sys

DEFUALT_PAD_LENGTH = 1028


def main():
    # Information on command line arguments from https://tutorialspoint.com/python/python_command_line_arguments.htm
    # Information on this syntax from https://stackoverflow.com/a/11479840 & https://www.udacity.com/blog/2021/10/python-match-case-statement-example-alternatives.html
    if len(sys.argv) < 2:
        sys.argv.append("-m")

    match sys.argv[1]:
        case "-m":
            user_manual()
        case "-p":
            user_new_pad()
        case "-e":
            user_encrypt()
        case "-d":
            user_decrypt()
        case _:
            user_manual()

# -------------------- CRYPTOGRAPHY FUNCTIONS --------------------


def generate_pad(length):
    """
    Take a length as argument, and make a
    random string of ASCII upercase
    charicters
    """
    pad = ""
    for i in range(0, length):
        pad += choice(string.ascii_uppercase)

    return pad


def encode(message, pad):
    # Start by snitizing the inputs. Make pad a list of numbers,
    # where A = 0, B = 1, C = 2 and so on.
    pad_numbers = []
    for num in pad:
        pad_numbers.append(ord(num) - 65)

    # Iterate over each alpha char of the message, shifting by pad_numbers[i]
    encoded_message = ""
    pad_pointer = 0
    for c in message:
        if c.isalpha():
            if c.isupper():
                encoded_message += chr((((ord(c) - 65) +  # Move the letter into number space,
                                         pad_numbers[pad_pointer]) % 26) + 65)  # shift over, move back into ASCII space
            else:
                encoded_message += chr((((ord(c) - 97) +
                                         pad_numbers[pad_pointer]) % 26) + 97)
            pad_pointer += 1
        else:
            encoded_message += c

    return encoded_message


def decode(message, pad):
    # Start by snitizing the inputs. Make pad a list of numbers,
    # where A = 0, B = 1, C = 2 and so on.
    pad_numbers = []
    for num in pad:
        pad_numbers.append(ord(num) - 65)

    # Iterate over each alpha char of the message, shifting by pad_numbers[i]
    encoded_message = ""
    pad_pointer = 0
    for c in message:
        if c.isalpha():
            if c.isupper():
                encoded_message += chr((((ord(c) - 65) -  # Move the letter into number space,
                                         pad_numbers[pad_pointer]) % 26) + 65)  # shift over, move back into ASCII space
            else:
                encoded_message += chr((((ord(c) - 97) -
                                         pad_numbers[pad_pointer]) % 26) + 97)
            pad_pointer += 1
        else:
            encoded_message += c

    return encoded_message

# -------------------- USER FUNCTIONS --------------------


def user_manual():
    print("Cipher.py uses the one time pad cipher to encrypy and decrypt messages. See useage below:")
    print("python3 cipher.py -m → Shows this manual")
    print(
        "python3 cipher.py -p [FILE].txt → Generates a onetime pad of the defualt lenght, 1028 charicters as FILE.txt")
    print(
        "python3 cipher.py -p [FILE].txt [NUMBER] → Generates a onetime pad of the length NUMBER,as FILE.txt")
    print(
        "python3 cipher.py -e [FILE].txt -w [PAD].txt → Encrypts FILE.txt with PAD.txt as it's one time pad")
    print(
        "python3 cipher.py -d [FILE].txt -w [PAD].txt → Decrypts FILE.txt with PAD.txt as it's one time pad")


def user_new_pad():
    # First, determine if the user is using the defualt length, or a custom length
    if len(sys.argv) == 4:
        pad_len = int(sys.argv[3])
    else:
        pad_len = DEFUALT_PAD_LENGTH

    pad_text = generate_pad(pad_len)
    try:
        # I am using x as my mode so that users do not accidentally overwrite a pad they have
        with open(sys.argv[2], "x") as pad_file:
            pad_file.write(pad_text)
    except FileExistsError:
        print(f"Error: {sys.argv[2]} already exsits.")

def user_encrypt():
    # Open both files and save them to variables
    with open(sys.argv[2]) as message_file:
        message = message_file.read()
    with open(sys.argv[4]) as pad_file:
        pad = pad_file.read()

    # Use the encode function
    encrypted_message = encode(message, pad)

    # Print this to the user
    print("---------- ENCRYPTED MESSAGE ----------")
    print(encrypted_message)

def user_decrypt():
     # Open both files and save them to variables
    with open(sys.argv[2]) as message_file:
        message = message_file.read()
    with open(sys.argv[4]) as pad_file:
        pad = pad_file.read()

    # Use the decode function
    decrypted_message = decode(message, pad)

    # Print this to the user
    print("---------- DECRYPTED MESSAGE ----------")
    print(decrypted_message)

if __name__ == "__main__":
    main()
