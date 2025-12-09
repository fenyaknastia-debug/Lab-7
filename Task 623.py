def find_min_max(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

# Користувач вводить числа без додаткового тексту
data = list(map(int, input().split()))

print("Вхідні числа:")
print(*data)

min_val, max_val = find_min_max(data)

print("Найменше і найбільше число:")
print(min_val, max_val)
