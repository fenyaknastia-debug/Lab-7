def is_leap_year(year):
    """
    Повертає True, якщо рік високосний, і False інакше.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Зчитування років
year1 = int(input())
year2 = int(input())

# Вивід вхідних даних
print("Вхідні дані:")
print(year1)
print(year2)

# Вивід результатів
print("Вихідні дані:")
print(is_leap_year(year1))
print(is_leap_year(year2))

