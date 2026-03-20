class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


# Main program
my_car = Car("ABC-123", 142)

print("Registration number:", my_car.registration_number)
print("Maximum speed:", my_car.maximum_speed, "km/h")
print("Current speed:", my_car.current_speed, "km/h")
print("Travelled distance:", my_car.travelled_distance, "km")