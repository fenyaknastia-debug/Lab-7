import math

# Функції для обчислення площ
def triangle_area(a, b, c):
    if a+b<=c or a+c<=b or b+c<=a:
        return None
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def circle_area(r):
    return math.pi*r**2

def rectangle_area(a, b):
    return a*b

def calculate_area(shape, numbers):
    if shape=="triangle":
        if len(numbers)!=3:
            return "triangle requires 3 sides"
        area = triangle_area(*numbers)
        return "triangle does not exist" if area is None else f"{area:.2f}"
    elif shape=="circle":
        if len(numbers)!=1:
            return "circle requires 1 radius"
        return f"{circle_area(numbers[0]):.2f}"
    elif shape=="rectangle":
        if len(numbers)!=2:
            return "rectangle requires 2 sides"
        return f"{rectangle_area(*numbers):.2f}"
    else:
        return "unknown shape"

# Зчитування даних від користувача
data = []
print("Вхідні дані:")

while True:
    shape = input().strip()
    if shape == "":  # кінець введення
        break
    numbers_line = input().strip()
    if numbers_line == "":
        numbers = []
    else:
        numbers = list(map(float, numbers_line.split()))
    data.append((shape, numbers))

# Вивід
print("Вихідні дані:")
for shape, numbers in data:
    print(calculate_area(shape, numbers))

