def round_standard(num):
    if num >= 0:
        sign = 1
    else:
        sign = -1
    return sign * int((abs(num) + 0.5))

# Тесты
print(round_standard(1.5))
print(round_standard(-2.5))
print(round_standard(1.6))
print(round_standard(5.11))