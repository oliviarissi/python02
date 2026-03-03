#!/usr/bin/env python3

def garden_operations() -> None:

    print("Testing ValueError...")
    try:
        nb1 = int("abc")
        print(nb1)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        nb2 = 10 / 0
        print(nb2)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        file_name = "missing.txt"
        fd = open(file_name)
        print(fd.read())
        fd.close()
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file_name}'\n")

    print("Testing KeyError...")
    test_dict = {
        "eng": "hello",
        "esp": "hola",
        "fr": "bon jour"
    }

    try:
        find = "missing\\_plant"
        print(test_dict[find])
    except KeyError:
        print(f"Caught KeyError: '{find}'\n")

    print("Testing multiple errors together...")
    try:
        test1 = int("abc")
        test2 = 10 / 0
        print(test1, test2)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    garden_operations()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
