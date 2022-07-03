
def plusOne(digits: list) -> list:
    digits = digits[::-1]
    one, i = 1, 0

    while one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = 0
        else:
            digits.append(1)
            one = 0
        i += 1
    return digits[::-1]


digits = [1, 2, 3]
# The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
print(plusOne(digits))  # Output: [1, 2, 4]

digits = [4, 3, 2, 1]
# The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
print(plusOne(digits))  # Output: [4, 3, 2, 2]

digits = [9]
# The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
print(plusOne(digits))  # Output: [1, 0]
