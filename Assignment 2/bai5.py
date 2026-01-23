import math

def unit_price_per_square_meter(diameter_cm, price):
    # Convert diameter from cm to meters
    radius_m = (diameter_cm / 100) / 2
    area = math.pi * radius_m ** 2
    return price / area


# Main program
diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (USD): "))

diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (USD): "))

unit_price1 = unit_price_per_square_meter(diameter1, price1)
unit_price2 = unit_price_per_square_meter(diameter2, price2)

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price2 < unit_price1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")

