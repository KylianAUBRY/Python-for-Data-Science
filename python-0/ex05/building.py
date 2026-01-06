import sys
import string


def main():
    """
    Analyzes the given text and prints information about its char composition.

    Asks for input if no argument is given:

    raises AssertionError: Too many arguments provided
    """
    if (len(sys.argv) > 2):
        print("AssertionError : more than one argument is provided.")
        return

    if (len(sys.argv) < 2):
        str = sys.stdin.read()

    else:
        str = sys.argv[1]
    upper = 0
    lower = 0
    digits = 0
    spaces = 0
    punctuation = 0

    for c in str:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digits += 1
        elif c.isspace():
            spaces += 1
        elif c in string.punctuation:
            punctuation += 1

    print(f"The text contains {len(str)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
