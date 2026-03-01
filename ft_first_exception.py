#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int | None:
    """Validate temp input (str), handle exceptions, return temp as int."""

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
    """Test temperature validation with valid and invalid inputs."""

    print("=== Garden Temperature Checker ===\n")

    test_values = ["25", "abc", "100", "-50"]

    for val in test_values:
        check_temperature(val)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
