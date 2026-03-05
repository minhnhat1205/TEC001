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


