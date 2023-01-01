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
    cipher = ''  # variable for cipher

    for letter in message:  # encrypt letter
        if letter != ' ':  # check for space
            cipher += morse_chars[letter] + ''  # add letter code to cipher
        else:
            cipher += ' '
    return cipher

def main():
    message = 'SOS'  # eng message
    result = encrypt(message.upper())  # uppercase result
    print(result)

main()