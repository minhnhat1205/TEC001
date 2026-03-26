class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator at floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator at floor: {self.current_floor}")

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        # Create elevators
        for _ in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
        elevator = self.elevators[elevator_number - 1]  # 1-based index
        elevator.go_to_floor(destination_floor)


# Main program
building = Building(1, 10, 3)

# Run elevators
building.run_elevator(1, 5)
building.run_elevator(2, 8)
building.run_elevator(3, 3)

# Move one elevator again
building.run_elevator(1, 1)