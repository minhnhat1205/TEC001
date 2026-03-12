numbers = []

while True:
    user_input = input("Enter a number (empty to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for number in numbers[:5]:
    print(number)