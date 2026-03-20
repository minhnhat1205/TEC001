class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        # Ensure speed does not exceed maximum speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        # Ensure speed does not go below 0
        if self.current_speed < 0:
            self.current_speed = 0


# Main program
my_car = Car("ABC-123", 142)

# Accelerations
my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)

print("Current speed:", my_car.current_speed, "km/h")

# Emergency brake
my_car.accelerate(-200)

print("Final speed after braking:", my_car.current_speed, "km/h")