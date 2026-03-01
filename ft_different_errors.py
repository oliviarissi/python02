#!/usr/bin/env python3

def garden_operations() -> None:

    print("Testing ValueError...")
        try:
            xx
        except (ValueError):
            print("Caught ValueError: invalid literal for int()")
    
    print("Testing ZeroDivisionError...")
        try:
            xx
        except (ZeroDivisionError):
            print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
        try:
            xx
        except (FileNotFoundError):
            print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("Testing KeyError...")
        try:
            xx
        except (KeyError):
            print("Caught KeyError: 'missing\_plant'")

    print("Testing multiple errors together...")
        try:
            xx
        except (ValueError, ZeroDivisionError):
            print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    
    garden_operations()

    print("All error types tested successfully!")

if __name__:"__main__"
    test_error_types()