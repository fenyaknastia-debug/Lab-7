def convert_if_upper(text, n, m):
    count_upper = sum(1 for c in text[:m] if c.isupper())
    return text.upper() if count_upper >= n else text

# Зчитування вхідних даних
line1 = input()
line2 = input()
line3 = input()
line4 = input()

# Вивід вхідних даних
print("Вхідні дані:")
print(line1)
print(line2)
print(line3)
print(line4)

# Вивід результатів
print("\nВихідні дані:")
print(convert_if_upper(line1, *map(int, line2.split())))
print(convert_if_upper(line3, *map(int, line4.split())))
