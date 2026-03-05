import re

def redact_phone_numbers(text):
    pattern = r'(\+84\d+|\b\d{10}\b)'
    result = re.sub(pattern, "[REDACTED]", text)
    return result


# Example
paragraph = "You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321,"
print(redact_phone_numbers(paragraph))