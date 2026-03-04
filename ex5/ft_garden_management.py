#!/usr/bin/env python3

class GardenError(Exception):
    """
    Base class for all garden-related errors.
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
        super().__init__("Not enough water in the tank")


class GardenManager:

    @staticmethod
    def add_plants(plant_list) -> None:
        """
        Add plants to the garden.

        Iterates over the plant list and adds them,
        raising an error for any `None` values.

        Parameters:
        plant_list (list): List of plant names to add.

        Returns:
        None
        """

        try:
            for plant in plant_list:
                if plant is None:
                    raise ValueError
                print(f"Added {plant} successfully")
        except ValueError:
            print("Error adding plant: Plant name cannot be empty!")
        finally:
            print(" ")

    @staticmethod
    def water_plants(plant_list) -> None:
        """
        Water the plants in the list.

        Iterates over the plant list, watering each plant.
        If a plant is `None`, it raises a `ValueError`.
        Ensures cleanup of the watering system after the operation.

        Parameters:
        plant_list (list): List of plant names to water.

        Returns:
        None
        """

        print("Opening watering system")

        try:
            for plant in plant_list:
                if plant is None:
                    raise ValueError
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(name, water, sunlight) -> str:
        """
        Check if a plant is healthy based on water level and sunlight hours.

        Validates the plant's conditions:
        - Water level must be between 1 and 10.
        - Sunlight hours must be between 2 and 12.
        - Raises `ValueError` if any condition is violated.

        Parameters:
        name (str): Name of the plant.
        water (int): Water level of the plant (1-10).
        sunlight (int): Sunlight hours received by the plant (2-12).

        Returns:
        str: A message indicating whether the plant is healthy.

        Raises:
        ValueError: If any condition is violated.
        """

        if name is None:
            raise ValueError("Plant name cannot be empty!")
        if water < 1 or water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        if sunlight < 2 or sunlight > 12:
            raise ValueError(f"Sunlight hours {sunlight} is too low (min 2)")

        return (f"{name}: healthy (water: {water}, sun: {sunlight})")


def test_garden_management() -> None:
    """
    Test the garden management system.

    Tests adding plants, watering plants, checking plant health,
    and error recovery. Demonstrates handling of various exceptions.

    Returns:
    None
    """

    plant_list = ["tomato", "lettuce", None,]

    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")

    GardenManager.add_plants(plant_list)

    print("Watering plants...")
    try:
        GardenManager.water_plants(plant_list)
    except ValueError:
        pass
    finally:
        print(" ")

    print("Checking plant health...")
    try:
        print(GardenManager.check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error checking tomato: {e}")

    try:
        print(GardenManager.check_plant_health("lettuce", 15, 8))
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print(" ")

    print("Testing error recovery...")

    try:
        raise WaterError
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
