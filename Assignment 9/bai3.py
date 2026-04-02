def calculate_average_score(filename):
    total = 0
    count = 0

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue  # skip empty lines

            name, score = line.split(",")
            total += float(score)
            count += 1

    if count == 0:
        return 0

    return total / count


# Example usage
file_name = "scores.txt"
average = calculate_average_score(file_name)

print("Average score:", average)