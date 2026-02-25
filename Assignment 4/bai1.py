numbers = []

while True:
    value = input("Enter a number (empty to quit): ")

    if value == "":
        break

    numbers.append(float(value))

numbers.sort(reverse=True)

print("The five greatest numbers are:")
for number in numbers[:5]:
    print(number)