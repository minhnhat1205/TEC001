import random

# 3-digit code (digits from 0 to 9)
code_3_digit = ""
for _ in range(3):
    code_3_digit += str(random.randint(0, 9))

# 4-digit code (digits from 1 to 6)
code_4_digit = ""
for _ in range(4):
    code_4_digit += str(random.randint(1, 6))

print("3-digit code:", code_3_digit)
print("4-digit code:", code_4_digit)
