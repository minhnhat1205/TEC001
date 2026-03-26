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


class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Reg':<10} {'Max':<6} {'Speed':<6} {'Distance':<10}")
        print("-" * 40)
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.maximum_speed:<6} {car.current_speed:<6} {int(car.travelled_distance):<10}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False


# Main program
cars = []
for i in range(1, 11):
    reg = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()

# Final result
print("\n🏁 Race finished!")
race.print_status()