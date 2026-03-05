def is_valid_hex_color(color):
    if len(color) != 7 or color[0] != "#":
        return False

    hex_digits = "0123456789ABCDEFabcdef"

    for char in color[1:]:
        if char not in hex_digits:
            return False

    return True