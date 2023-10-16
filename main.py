# Sachin Karki
# Assignment 7, Creating Bike Class

# importing bike class from bike.py
from bike import Bike

try:
    # Instantiating our Bike, gear: 10, wheels: 3, brake type: "foot"
    my_bike = Bike(10, 3, "foot")

    # Printing our bike info
    print("Our new bike")
    print(f"Number of Gears: {my_bike.get_number_of_gears()}")
    print(f"Number of Wheels: {my_bike.get_number_of_wheels()}")
    print(f"Brake Type: {my_bike.get_brake_type()}")
    print(f"Current Gear: {my_bike.get_current_gear()}")
    input("Continue")
    print()
    # Setting the current gear at 8
    print("Setting Our Current Gear at 8")
    my_bike.set_current_gear(8)
    print(f"Our Current Gear: {my_bike.get_current_gear()}")
    input("Continue")
    print()
    # Increasing the current gear
    print("Let's Rev Up and Increase the Gear")
    my_bike.increase_gear()
    print(f"Our Current Gear: {my_bike.get_current_gear()}")
    input("Continue")
    print()
    # Increasing the gear at Max
    print("MAX Gear")
    my_bike.increase_gear()
    print(f"Our Current Gear: {my_bike.get_current_gear()}")
    input("Continue")
    print()
    # Resetting gear
    print("Resetting our gear to 2")
    my_bike.set_current_gear(2)
    print(f"Our Current Gear: {my_bike.get_current_gear()}")
    input("Continue")
    print()
    # Decreasing current gear
    print("Decreasing Our Current Gear")
    my_bike.decrease_gear()
    print(f"Our Current Gear: {my_bike.get_current_gear()}")
    input("Continue")
    print()

# Catching exception
except Exception as e:
    print(f"Error message: {e}")