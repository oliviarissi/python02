#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """
    Check plant health based on water level and sunlight hours.

    Validates the plant's health conditions based on the following criteria:
    - Plant name cannot be None.
    - Water level must be between 1 and 10 (inclusive).
    - Sunlight hours must be between 2 and 12 (inclusive).

    Parameters:
    plant_name (str): The name of the plant.
    water_level (int): The current water level (1-10).
    sunlight_hours (int): The hours of sunlight the plant receives (2-12).

    Returns:
    str: A message indicating whether the plant is healthy.

    Raises:
    ValueError: If any condition is violated.
    """

    if plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")

    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Test the plant health check function with various inputs.

    Tests normal and error scenarios for plant name,
    water level, and sunlight hours.
    Prints results of each test.

    Returns:
    None
    """

    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(f"{check_plant_health("tomato", 5, 5)}\n")
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing empty plant name...")
    try:
        print(f"{check_plant_health(None, 5, 5)}\n")
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad water level...")
    try:
        print(f"{check_plant_health("tomato", 15, 5)}\n")
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad sunlight hours...")
    try:
        print(f"{check_plant_health("tomato", 5, 0)}\n")
    except ValueError as e:
        print(f"Error: {e}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
