import random

# Ask the user for the number of random points
N = int(input("How many random points to generate? "))

points_inside_circle = 0

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        points_inside_circle += 1

# Calculate approximation of pi
pi_approx = 4 * points_inside_circle / N

print("Approximation of pi:", pi_approx)