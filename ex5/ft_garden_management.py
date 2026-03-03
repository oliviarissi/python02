#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank")


class GardenManager:

    @staticmethod
    def add_plants(plant_list) -> None:
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
        if name is None:
            raise ValueError("Plant name cannot be empty!")
        if water < 1 or water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        if sunlight < 2 or sunlight > 12:
            raise ValueError(f"Sunlight hours {sunlight} is too low (min 2)")

        return (f"{name}: healthy (water: {water}, sun: {sunlight})")


def test_garden_management() -> None:

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
