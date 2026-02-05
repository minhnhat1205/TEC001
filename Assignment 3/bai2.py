while True:
    inches = float(input("Enter inches: "))

    if inches < 0:
        print("Program ended.")
        break

    centimeters = inches * 2.54
    print(inches, "inches is", centimeters, "centimeters")
