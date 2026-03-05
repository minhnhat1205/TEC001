import re

def sum_numbers_in_text(text):
    numbers = re.findall(r'\d+', text)  # find all numbers
    total = 0

    for num in numbers:
        total += int(num)

    return total


# Example
paragraph = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
print(sum_numbers_in_text(paragraph))