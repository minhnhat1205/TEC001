import random

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


# Create 10 cars
cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg_number, max_speed))

# Race simulation
race_on = True

while race_on:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_on = False

# Print results in table format
print(f"{'Reg Number':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<10}")
print("-" * 45)

for car in cars:
    print(f"{car.registration_number:<10} {car.maximum_speed:<10} {car.current_speed:<10} {int(car.travelled_distance):<10}")