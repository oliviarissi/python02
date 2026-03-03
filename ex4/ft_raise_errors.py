#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    if plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")

    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:

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
