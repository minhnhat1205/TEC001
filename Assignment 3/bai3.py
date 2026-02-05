numbers = []

while True:
    value = input("Enter a number (empty to quit): ")

    if value == "":
        break

    numbers.append(float(value))

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")
