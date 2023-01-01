import string

alphabet = list(string.ascii_lowercase)  # Eng Alphabet


def encrypt():
    originalText = 'a'
    cipher = ''
    shift = +3
    for letter in originalText.lower():
        if letter != ' ':
            cipher += (chr(ord(letter) + shift))
    print(cipher)


encrypt()
