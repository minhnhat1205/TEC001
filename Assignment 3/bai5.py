def middle_characters(text):
    length = len(text)
    middle = length // 2

    if length % 2 == 0:
        return text[middle - 1: middle + 1]
    else:
        return text[middle]
