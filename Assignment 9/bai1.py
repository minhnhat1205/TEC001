def count_non_empty_lines(filename):
    count = 0

    with open(filename, "r") as file:
        for line in file:
            if line.strip() != "":  # ignore blank lines
                count += 1

    return count


# Example usage
file_name = "example.txt"
print("Number of non-empty lines:", count_non_empty_lines(file_name))