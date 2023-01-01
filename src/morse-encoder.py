morse_chars = {'A': '.-', 'B': '-...',
               'C': '-.-.', 'D': '-..', 'E': '.',
               'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.---', 'K': '-.-',
               'L': '.-..', 'M': '--', 'N': '-.',
               'O': '---', 'P': '.--.', 'Q': '--.-',
               'R': '.-.', 'S': '...', 'T': '-',
               'U': '..-', 'V': '...-', 'W': '.--',
               'X': '-..-', 'Y': '-.--', 'Z': '--..',
               '1': '.----', '2': '..---', '3': '...--',
               '4': '....-', '5': '.....', '6': '-....',
               '7': '--...', '8': '---..', '9': '----.',
               '0': '-----', ', ': '--..--', '.': '.-.-.-',
               '?': '..--..', '/': '-..-.', '-': '-....-',
               '(': '-.--.', ')': '-.--.-'}


def encrypt(message):  # from eng to morse
    cipher = ''  # var for cipher

    for letter in message:  # encrypt letter
        if letter != ' ':  # check for space
            cipher += morse_chars[letter] + ''  # add letter code to cipher
        else:
            cipher += ' '
    return cipher


def decrypt(message):  # from morse to eng
    decipher = ''  # var for deciphering
    message += ' '
    citext = ''  # text of morse

    for letter in message:  # decrypt letter
        if letter != ' ':  # check for space
            i = 0
            citext += letter
        else:
            i += 1  # new character
            if i == 2:  # new word
                decipher += ' '
            else:
                decipher += list(morse_chars.keys())[list(morse_chars.values()).index(citext)]
                citext = ''  # clear
    return decipher


def main():
    choice = int(input("1  ENG -> MORSE"
                       "2  MORSE"
                       "Your choice (1 or 2):  "))
    if choice == 1:
        message = 'SOS'  # eng message
        result = encrypt(message.upper())  # uppercase result
        print(result)
    elif choice == 2:
        message = '... --- ...'
        result = decrypt(message)
        print(result)


main()
