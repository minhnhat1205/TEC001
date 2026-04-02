def find_keyword_lines(filename, keyword):
    line_numbers = []

    with open(filename, "r") as file:
        for i, line in enumerate(file, start=1):  # 1-based index
            if keyword in line:
                line_numbers.append(i)

    return line_numbers


# Example usage
file_name = "example.txt"
keyword = "Python"

result = find_keyword_lines(file_name, keyword)
print("Keyword found on lines:", result)