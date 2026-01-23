def check_zander_size():
    length = float(input("Enter the length of the zander (cm): "))

    size_limit = 42

    if length < size_limit:
        difference = size_limit - length
        print("The zander is too small.")
        print("Release the fish back into the lake.")
        print("It is", difference, "cm below the size limit.")
    else:
        print("The zander meets the size limit. You may keep it.")

# Call the function
check_zander_size()
