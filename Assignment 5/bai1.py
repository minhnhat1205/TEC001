def valid_course_code(code):
    if len(code) not in [5, 6]:
        return False

    letters = code[:-3]
    digits = code[-3:]

    if (len(letters) in [2, 3] and
        letters.isupper() and letters.isalpha() and
        digits.isdigit()):
        return True
    else:
        return False