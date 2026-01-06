import sys


def main():
    """
    Accepts only 1 arguments:
    1. string

    takes a string as an argument and encodes it into Morse Code.
    """
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    if len(sys.argv) != 2:
        print("AssertionError: The number of arguments is incorrect; \
              1 arguments are expected.")
        return
    text = sys.argv[1]

    for char in text:
        if char.upper() not in morse_code_dict:
            print("AssertionError: The string contains \
            unsupported characters.")
            return
    morse_code = ' '.join(morse_code_dict[char.upper()] for char in text)

    print(morse_code)


if __name__ == "__main__":
    main()
