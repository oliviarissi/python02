#!/usr/bin/env python3

def water_plants(plant_list) -> None:
    """
    Water plants in the given list.

    Iterates over the plant list, waters each plant, and raises a ValueError
    if any plant is `None`. Ensures cleanup happens after the operation.

    Parameters:
    plant_list (list): List of plant names to water.

    Returns:
    None

    Raises:
    ValueError: If `None` is found in the plant list.
    """

    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError
            print(f"Watering {plant}")
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Test the watering system with valid and invalid plant lists.

    Demonstrates normal watering and handles the `ValueError` when `None`
    is in the list, ensuring cleanup is done even if errors occur.

    Returns:
    None
    """

    plant_list_ok = ["tomato", "lettuce", "carrots",]
    plant_list_not_ok = ["tomato", None, "carrots",]

    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    try:
        water_plants(plant_list_ok)
        print("Watering completed successfully!")
    except ValueError:
        pass
    finally:
        print(" ")

    print("Testing with error...")
    try:
        water_plants(plant_list_not_ok)
    except ValueError:
        pass
    finally:
        print(" ")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
