# Declaring Bike Class
class Bike:

  # Defining private properties
  num_gears = 4
  current_gear = 1  #default gear
  num_wheels = 2
  brake_type = "foot"

  # Class instantiator
  def __init__(self, number_of_gears=1, number_of_wheels=2, brake_type="hand"):

    # Setting properties
    self.set_number_of_gears(number_of_gears)
    self.set_number_of_wheels(number_of_wheels)
    self.set_brake_type(brake_type)
    self.set_current_gear(1)

  # Getter for the num_gears
  def get_number_of_gears(self):
    return self.num_gears

  # Setter for the num_gears (integer from 1 to 15)
  def set_number_of_gears(self, number_of_gears):
    try:
      if int(number_of_gears):
        pass
    except Exception as e:
      raise ValueError(f"{number_of_gears} is not a valid integer")

  # Condition to confirm if it is between 1 and 15
    if 1 <= number_of_gears <= 15:
      self.num_gears = number_of_gears
    else:
      raise ValueError(f"{number_of_gears} is not between 1 and 15")
# Getter for the current_gear

  def get_current_gear(self):
    return self.current_gear

# Setter for the current_gear

  def set_current_gear(self, current_gear):
    try:
      # Condition to see if its an integer
      if int(current_gear):
        pass
    except Exception as e:
      raise ValueError(f"{current_gear} is not a valid integer")

  # Condition to confirm self.num_gears
    if 1 <= current_gear <= self.num_gears:
      self.current_gear = current_gear
    else:
      raise ValueError(f"{current_gear} is not between 1 and {self.num_gears}")

# Getter for the num_wheels

  def get_number_of_wheels(self):
    return self.num_wheels

# Setter for the num_wheels (integer from 1 to 15)

  def set_number_of_wheels(self, number_of_wheels):
    try:
      # Condition to confirm if its an integer
      if int(number_of_wheels):
        pass
    except Exception as e:
      raise ValueError(f"{number_of_wheels} is not a valid integer")

# Condition to confirm if it is between 1 and 4?
    if 1 <= number_of_wheels <= 4:
      self.num_wheels = number_of_wheels
    else:
      raise ValueError(f"{number_of_wheels} is not between 1 and 4")

# Getter for the brake_type

  def get_brake_type(self):
    return self.brake_type

# Setter for the brake_type, only acceptable values are "hand" or "foot"

  def set_brake_type(self, brake_type):
    try:
      if isinstance(brake_type, str):
        pass
    except Exception as e:
      raise ValueError(f"{brake_type} is not a string")
    if brake_type in ["hand", "foot"]:
      self.brake_type = brake_type
    else:
      raise ValueError(f"{brake_type} is not either 'hand' or 'foot")

# Increasing the gear

  def increase_gear(self):
    if self.get_current_gear() < self.num_gears:
      self.set_current_gear(self.get_current_gear() + 1)


# Decreasing the gear

  def decrease_gear(self):
    if self.get_current_gear() > 1:
      self.set_current_gear(self.get_current_gear() - 1)
