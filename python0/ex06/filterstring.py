import sys
from ft_filter import ft_filter


def main():
    """
    Accepts only 2 arguments:
    1. string
    2. integer

    Returns a list of words that are longer than the integer.
    """
    if len(sys.argv) != 3:
        print("AssertionError: The number of arguments is incorrect; \
              2 arguments are expected.")
        return
    text = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: The argument type is incorrect.")
        return

    if not isinstance(text, str) or not isinstance(n, int):
        print("AssertionError: The argument type is incorrect.")
        return

    filtered_word = list(ft_filter(lambda x: len(x) > n, text.split()))

    print(filtered_word)


if __name__ == "__main__":
    main()
