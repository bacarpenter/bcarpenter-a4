# bcarpenter-a4 | cipher.py

`cipher.py` is a command line utility used to encrypt and decrypt messages with the one time pad cipher. You can create a new pad to encrypt secret messages, and use an old pad to decrypt messages that someone passed to you! 

# Usage

> Note, you can find a manual with the command
> ```zsh
> python3 cipher.py -m
>```

## Create Pads
To encrypt a message, first, create a new pad with the command

```zsh
python3 cipher.py -p [FILE].txt [LENGTH]
```

Where `[FILE].txt` is the path to where you want your new file stored,and [LENGTH], is an integer for how long you want your pad to be. If left blank, the program will default to 1028.

*Remember: Your pad must be as long or longer than the message you want to encode. If your message is 128 characters long, your pad must be at least 128 characters long!*

Example syntax:

```zsh
python3 cipher.py -p my_pad.txt 5674
```

## Encode messages
To encode a message, you will need your message in a text file, along with the pad you would like to use.

```zsh
python3 cipher.py -e [FILE].txt -w [PAD].txt
```

Where `[FILE].txt` is the path to the message you want to encrypt, and `[PAD].txt` is the pad you will use for encryption.

Example syntax:

```zsh
python3 cipher.py -e my_message.txt -w my_pad.txt
```

## Decode messages
To decode a message, you will need to encrypted message and the pad used for it's encryption.

```zsh
python3 cipher.py -d [FILE].txt -w [PAD].txt
```

Where `[FILE].txt` is the path to the encrypted message, and `[PAD].txt` is the pad used for it's encryption.

Example syntax:

```zsh
python3 cipher.py -d secret_message.txt -w my_pad.txt
```

# Testing 

To run the included unit tests, run `pytest` in your console!

# Note

Please note that this is a submission for Prof. Brewer's CSC-151 Programming Language Concepts class, at Smith College.