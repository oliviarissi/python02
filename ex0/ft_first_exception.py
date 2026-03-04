#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int | None:
    """
    Validate and convert temperature input.

    Converts temp_str to int, checks if within range (0-40°C),
    raises ValueError if invalid or out of range.

    Parameters:
    temp_str (str): Temperature as string.

    Returns:
    int | None: Valid temperature or None if invalid.
    """

    print(f"Testing temperature: {temp_str}")

    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: {temp_str} is not a valid number\n")
        return None

    if temp < 0:
        print(f"{temp}°C is too cold for plants (min 0°C)\n")
        return None

    if temp > 40:
        print(f"{temp}°C is too hot for plants (max 40°C)\n")
        return None

    print(f"Temperature {temp}°C is perfect for plants!\n")
    return temp


def test_temperature_input() -> None:
    """
    Run tests on check_temperature.

    Tests multiple cases to ensure validation works.

    Returns:
    None
    """

    print("=== Garden Temperature Checker ===\n")

    test_values = ["25", "abc", "100", "-50"]

    for val in test_values:
        check_temperature(val)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
