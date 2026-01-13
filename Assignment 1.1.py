name = input("Enter your name: ")
print("Hello " + name)

import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print("The circumference of the circle is:", circumference)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print("The perimeter of the rectangle is:", perimeter)
print("The area of the rectangle is:", area)

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum_numbers = num1 + num2 + num3
product = num1 * num2 * num3
average = sum_numbers / 3

print("Sum:", sum_numbers)
print("Product:", product)
print("Average:", average)

# Ask for input
talents = int(input("Enter talents: "))
pounds = int(input("Enter pounds: "))
lots = int(input("Enter lots: "))

# Convert everything to lots
total_lots = talents * 20 * 32 + pounds * 32 + lots

# Convert lots to grams
total_grams = total_lots * 13.3

# Convert grams to kilograms and remaining grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

# Output result
print("The weight is", kilograms, "kilograms and", round(grams, 2), "grams.")

import random

# 3-digit code (digits from 0 to 9)
code_3_digit = ""
for _ in range(3):
    code_3_digit += str(random.randint(0, 9))

# 4-digit code (digits from 1 to 6)
code_4_digit = ""
for _ in range(4):
    code_4_digit += str(random.randint(1, 6))

print("3-digit code:", code_3_digit)
print("4-digit code:", code_4_digit)
