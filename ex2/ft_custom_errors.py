#!/usr/bin/env python3

class GardenError(Exception):
    """
    Base class for all custom garden-related errors.
    """

    pass


class PlantError(GardenError):
    """
    Raised when a plant error occurs (e.g., wilting).
    """

    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    """
    Raised when there is not enough water in the tank.
    """

    def __init__(self):
        super().__init__("Not enough water in the tank!")


def check_plant() -> None:
    """
    Simulate a plant error (wilting plant).

    Raises:
    PlantError: Simulates a wilting plant error.
    """

    raise PlantError


def check_water() -> None:
    """
    Simulate a water error (insufficient water).

    Raises:
    WaterError: Simulates a water shortage error.
    """

    raise WaterError


def test_errors() -> None:
    """
    Test custom garden-related errors.

    Demonstrates catching `PlantError`, `WaterError`,
    and the base `GardenError`.

    Returns:
    None
    """

    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
