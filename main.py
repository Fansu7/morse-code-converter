# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
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


#Takes an input from the user and convert the text to morse code.
def morse_encryption(text):
    morse_text = ''
    for element in text:
        if element != ' ':
            morse_text += MORSE_CODE_DICT[element] + ' '
        else:
            morse_text += element
    return morse_text


#This function takes an input from the user in morse code and decipher it
def morse_decryption(text):
    word = ''
    decipher_text = ''
    for element in text + ' ':
        if element != ' ':
            espacios = 0
            word += element
        else:
            espacios += 1
            if espacios == 2:
                decipher_text += ' '
            else:
                decipher_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(word)]
                word = ''
    return decipher_text.lower()


#"Main program" function
def morse_conversor():
    choice = input('Do you want to encrypt or decrypt?\n').lower()
    if choice == 'encrypt':
        user_text = input('Write whatever you want to encrypt: ').upper()
        print(morse_encryption(user_text))
    elif choice == 'decrypt':
        user_text = input('Write whatever you want to decrypt: ').upper()
        print(morse_decryption(user_text))
    else:
        print('"encrypt" or "decrypt" are the only available choices. Please try again.')
        morse_conversor()


morse_conversor()
