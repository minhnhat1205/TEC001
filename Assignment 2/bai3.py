def check_hemoglobin():
    sex = input("Enter biological sex (female/male): ").lower()
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        if hemoglobin < 117:
            print("Hemoglobin level is low.")
        elif hemoglobin > 155:
            print("Hemoglobin level is high.")
        else:
            print("Hemoglobin level is normal.")
    elif sex == "male":
        if hemoglobin < 134:
            print("Hemoglobin level is low.")
        elif hemoglobin > 167:
            print("Hemoglobin level is high.")
        else:
            print("Hemoglobin level is normal.")
    else:
        print("Invalid biological sex.")

# Call the function
check_hemoglobin()
