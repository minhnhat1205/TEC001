def caesar_cipher_file(filename, shift, direction):
    # Adjust shift direction
    if direction.lower() == "left":
        shift = -shift

    with open(filename, "r") as file:
        text = file.read()

    result = ""

    for char in text:
        if char.isupper():
            # Uppercase letters
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        elif char.islower():
            # Lowercase letters
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        elif char.isdigit():
            # Keep numbers unchanged
            result += char
        else:
            # Keep spaces, punctuation unchanged
            result += char

    # Save result to a new file
    output_file = "ciphertext.txt"
    with open(output_file, "w") as file:
        file.write(result)

    print("Ciphertext saved to", output_file)


# Example usage
caesar_cipher_file("input.txt", 3, "right")