class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# Main program
my_car = Car("ABC-123", 142)

# Accelerate
my_car.accelerate(60)

# Drive for 1.5 hours
my_car.drive(1.5)

print("Current speed:", my_car.current_speed, "km/h")
print("Travelled distance:", my_car.travelled_distance, "km")