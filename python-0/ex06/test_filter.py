from ft_filter import ft_filter


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


def main():
    ages = [5, 12, 17, 18, 24, 32]
    adults = ft_filter(myFunc, ages)

    for x in adults:
        print(x)
    print("-----filter----")
    adults = filter(myFunc, ages)

    for x in adults:
        print(x)

    print("--------------")
    bool = [0, 1, "", None, "Hello", 42, [], [1, 2, 3]]
    filtered_bool = ft_filter(None, bool)
    for x in filtered_bool:
        print(x)
    print("----filter----")
    filtered_bool = filter(None, bool)
    for x in filtered_bool:
        print(x)


if __name__ == "__main__":
    main()
