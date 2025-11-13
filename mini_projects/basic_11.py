# Build a Caesar Cipher

# Tips
# The idea is to encrypt a text by swapping the words
# chr() num ASCII into char
# ord() char into num ASCII


def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    print(result)


def decrypt(text, shift):
    return encrypt(text, -shift)

# encrypt("Hello dude", 6)

# decrypt("Nkrru jajk", 6)
